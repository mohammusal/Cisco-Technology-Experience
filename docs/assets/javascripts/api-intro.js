/* Offline interactive engine for Day 2 Lab 0 (API Core Principles).
   Activates ONLY on pages containing #api-intro-root. Zero external dependencies or URLs. */
(function () {
  "use strict";

  function isEditableTarget(el) {
    if (!el) return false;
    var tag = el.tagName;
    return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || el.isContentEditable;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function init() {
    var root = document.getElementById("api-intro-root");
    if (!root || root.dataset.apiIntroReady === "1") return;
    root.dataset.apiIntroReady = "1";

    initPresentMode(root);
    initAnatomyExplorer(root);
    initPlayground(root);
    initFlipCards(root);
    initCodeReviewQuiz(root);
  }

  /* =========================================================================
     1. PRESENT MODE (Dual-Mode Stage + 30:00 Pacing Timer)
     ========================================================================= */
  function initPresentMode(root) {
    var beats = Array.prototype.slice.call(root.querySelectorAll(".api-beat"));
    if (!beats.length) return;

    var startBtn = document.getElementById("api-start-present");
    var hud = document.getElementById("api-hud");
    var prevBtn = document.getElementById("api-hud-prev");
    var nextBtn = document.getElementById("api-hud-next");
    var exitBtn = document.getElementById("api-hud-exit");
    var selectEl = document.getElementById("api-hud-select");
    var progressBar = document.getElementById("api-hud-progress");
    var timerDisplay = document.getElementById("api-timer-display");
    var timerToggle = document.getElementById("api-timer-toggle");
    var timerReset = document.getElementById("api-timer-reset");

    var currentIndex = 0;
    var presenting = false;
    var totalSeconds = 30 * 60;
    var remainingSeconds = totalSeconds;
    var timerHandle = null;

    if (selectEl) {
      selectEl.innerHTML = "";
      beats.forEach(function (beat, idx) {
        var opt = document.createElement("option");
        opt.value = String(idx);
        var title = beat.getAttribute("data-title") || ("Beat " + (idx + 1));
        opt.textContent = (idx + 1) + " / " + beats.length + " — " + title;
        selectEl.appendChild(opt);
      });
    }

    function renderTimer() {
      if (!timerDisplay) return;
      var mins = Math.floor(remainingSeconds / 60);
      var secs = remainingSeconds % 60;
      timerDisplay.textContent =
        (mins < 10 ? "0" : "") + mins + ":" + (secs < 10 ? "0" : "") + secs;
    }

    function stopTimer() {
      if (timerHandle) {
        clearInterval(timerHandle);
        timerHandle = null;
      }
      if (timerToggle) timerToggle.textContent = "Start";
    }

    function toggleTimer() {
      if (timerHandle) {
        stopTimer();
        return;
      }
      if (timerToggle) timerToggle.textContent = "Pause";
      timerHandle = setInterval(function () {
        if (remainingSeconds > 0) {
          remainingSeconds -= 1;
          renderTimer();
        } else {
          stopTimer();
        }
      }, 1000);
    }

    function showBeat(idx) {
      currentIndex = Math.max(0, Math.min(beats.length - 1, idx));
      beats.forEach(function (beat, i) {
        beat.classList.toggle("is-active", i === currentIndex);
      });
      if (selectEl) selectEl.value = String(currentIndex);
      if (prevBtn) prevBtn.disabled = currentIndex === 0;
      if (nextBtn) nextBtn.disabled = currentIndex === beats.length - 1;
      if (progressBar) {
        progressBar.style.width = (((currentIndex + 1) / beats.length) * 100) + "%";
      }
      root.scrollTop = 0;
    }

    function enterPresent(idx) {
      presenting = true;
      document.body.classList.add("api-present-mode");
      if (hud) hud.setAttribute("aria-hidden", "false");
      showBeat(typeof idx === "number" ? idx : currentIndex);
    }

    function exitPresent() {
      presenting = false;
      document.body.classList.remove("api-present-mode");
      if (hud) hud.setAttribute("aria-hidden", "true");
      stopTimer();
    }

    if (startBtn) {
      startBtn.addEventListener("click", function () {
        enterPresent(0);
      });
    }
    if (prevBtn) prevBtn.addEventListener("click", function () { showBeat(currentIndex - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { showBeat(currentIndex + 1); });
    if (exitBtn) exitBtn.addEventListener("click", exitPresent);
    if (selectEl) {
      selectEl.addEventListener("change", function () {
        showBeat(parseInt(selectEl.value, 10) || 0);
      });
    }
    if (timerToggle) timerToggle.addEventListener("click", toggleTimer);
    if (timerReset) {
      timerReset.addEventListener("click", function () {
        stopTimer();
        remainingSeconds = totalSeconds;
        renderTimer();
      });
    }

    document.addEventListener("keydown", function (e) {
      if (isEditableTarget(e.target)) return;
      if (e.metaKey || e.ctrlKey || e.altKey) return;

      if (e.key === "p" || e.key === "P") {
        e.preventDefault();
        if (presenting) exitPresent();
        else enterPresent(currentIndex);
      } else if (presenting && (e.key === "ArrowRight" || e.key === "PageDown")) {
        e.preventDefault();
        showBeat(currentIndex + 1);
      } else if (presenting && (e.key === "ArrowLeft" || e.key === "PageUp")) {
        e.preventDefault();
        showBeat(currentIndex - 1);
      } else if (presenting && e.key === "Escape") {
        e.preventDefault();
        exitPresent();
      }
    });

    renderTimer();

    // Optional deep-link for classroom bookmarking or testing: ?present=1&beat=5
    try {
      var params = new URLSearchParams(window.location.search);
      if (params.get("present") === "1") {
        var b = parseInt(params.get("beat") || "1", 10);
        enterPresent(isNaN(b) ? 0 : b - 1);
      }
    } catch (_) {
      /* ignore URLSearchParams errors on older engines */
    }
  }

  /* =========================================================================
     2. REQUEST / RESPONSE ANATOMY EXPLORER (Beat 3)
     ========================================================================= */
  function initAnatomyExplorer(root) {
    var parts = Array.prototype.slice.call(root.querySelectorAll(".api-part"));
    var badgeEl = document.getElementById("api-anatomy-badge");
    var titleEl = document.getElementById("api-anatomy-title");
    var descEl = document.getElementById("api-anatomy-desc");
    var pitfallEl = document.getElementById("api-anatomy-pitfall");
    if (!parts.length || !titleEl) return;

    var DETAILS = {
      "req-verb": {
        badge: "Request · Part 1",
        title: "HTTP Verb (Method) — POST",
        desc: "Tells the server WHAT action you want to perform. POST means 'create a brand-new resource'.",
        pitfall: "Beginner pitfall: using GET when creating or deleting data. GET should ONLY read data."
      },
      "req-url": {
        badge: "Request · Part 2",
        title: "Endpoint URL — /v1/orders",
        desc: "Tells the server WHERE the resource lives. Notice the version (/v1/) and plural noun (/orders).",
        pitfall: "Beginner pitfall: a single typo (/v1/order instead of /v1/orders) usually triggers a 404 Not Found."
      },
      "req-headers": {
        badge: "Request · Part 3",
        title: "Headers — Metadata & Authentication",
        desc: "Key-value stickers on the outside of the envelope: 'Content-Type' says the body is JSON; 'Authorization' proves who you are.",
        pitfall: "Beginner pitfall: forgetting the word 'Bearer ' before a token, or putting secret keys in the URL."
      },
      "req-body": {
        badge: "Request · Part 4",
        title: "JSON Request Body — The Payload",
        desc: "The actual data you are sending to create or update a resource. GET and DELETE normally have no body.",
        pitfall: "Beginner pitfall: using single quotes instead of double quotes in JSON, or leaving a trailing comma."
      },
      "res-status": {
        badge: "Response · Part 1",
        title: "Status Code — 201 Created",
        desc: "A 3-digit traffic light telling your app what happened before it even parses the JSON. 201 means 'success, new item created!'.",
        pitfall: "Beginner pitfall: only checking for 200 OK — POST endpoints often return 201 Created instead."
      },
      "res-headers": {
        badge: "Response · Part 2",
        title: "Response Headers",
        desc: "Server metadata about the reply — for example telling your app that the body is JSON or how many requests you have left.",
        pitfall: "Good to know: rate-limit info (like Retry-After) lives in response headers too."
      },
      "res-body": {
        badge: "Response · Part 3",
        title: "JSON Response Body",
        desc: "The structured answer from the server — including the brand-new ID (#103) and status assigned by the server.",
        pitfall: "Pro habit: always inspect the response JSON on errors too — good APIs tell you exactly what went wrong."
      }
    };

    function selectPart(key) {
      var info = DETAILS[key];
      if (!info) return;
      parts.forEach(function (btn) {
        btn.classList.toggle("is-selected", btn.getAttribute("data-part") === key);
      });
      if (badgeEl) badgeEl.textContent = info.badge;
      titleEl.textContent = info.title;
      if (descEl) descEl.textContent = info.desc;
      if (pitfallEl) pitfallEl.textContent = info.pitfall;
    }

    parts.forEach(function (btn) {
      btn.addEventListener("click", function () {
        selectPart(btn.getAttribute("data-part"));
      });
    });

    selectPart("req-verb");
  }

  /* =========================================================================
     3. LIVE OFFLINE CAMPUS PIZZA API PLAYGROUND (Beat 5)
     ========================================================================= */
  function initPlayground(root) {
    var verbEl = document.getElementById("api-pg-verb");
    var pathEl = document.getElementById("api-pg-path");
    var authEl = document.getElementById("api-pg-auth");
    var authPreview = document.getElementById("api-pg-auth-preview");
    var bodyWrap = document.getElementById("api-pg-body-wrap");
    var bodyEl = document.getElementById("api-pg-body");
    var sendBtn = document.getElementById("api-pg-send");
    var resetBtn = document.getElementById("api-pg-reset");
    var statusEl = document.getElementById("api-pg-status");
    var metaEl = document.getElementById("api-pg-meta");
    var resBodyEl = document.getElementById("api-pg-res-body");
    var menuTbody = document.getElementById("api-db-menu");
    var ordersTbody = document.getElementById("api-db-orders");
    if (!verbEl || !pathEl || !sendBtn) return;

    var state = null;
    var lastHighlight = { table: null, id: null };

    function seedState() {
      state = {
        nextOrderId: 103,
        menu: [
          { id: 1, name: "Margherita", category: "pizza", price: 28 },
          { id: 2, name: "Pepperoni", category: "pizza", price: 34 },
          { id: 3, name: "Veggie", category: "pizza", price: 30 },
          { id: 4, name: "Iced Latte", category: "drink", price: 14 }
        ],
        orders: [
          { id: 101, customer: "Ola", item: "Margherita", status: "preparing" },
          { id: 102, customer: "Jan", item: "Pepperoni", status: "ready" }
        ]
      };
      lastHighlight = { table: null, id: null };
    }

    function renderDb() {
      if (menuTbody) {
        menuTbody.innerHTML = state.menu.map(function (m) {
          var cls = (lastHighlight.table === "menu" && lastHighlight.id === m.id) ? " class=\"api-db-row--flash\"" : "";
          return "<tr" + cls + "><td>" + m.id + "</td><td>" + escapeHtml(m.name) +
            "</td><td>" + escapeHtml(m.category) + "</td><td>" + m.price + " zl</td></tr>";
        }).join("") || "<tr><td colspan=\"4\">(empty)</td></tr>";
      }
      if (ordersTbody) {
        ordersTbody.innerHTML = state.orders.map(function (o) {
          var cls = (lastHighlight.table === "orders" && lastHighlight.id === o.id) ? " class=\"api-db-row--flash\"" : "";
          return "<tr" + cls + "><td>#" + o.id + "</td><td>" + escapeHtml(o.customer) +
            "</td><td>" + escapeHtml(o.item) + "</td><td><code>" + escapeHtml(o.status) + "</code></td></tr>";
        }).join("") || "<tr><td colspan=\"4\">(no orders yet)</td></tr>";
      }
    }

    function syncControls() {
      var v = verbEl.value;
      if (bodyWrap) bodyWrap.hidden = !(v === "POST" || v === "PATCH" || v === "PUT");
      if (authPreview) {
        authPreview.textContent = authEl && authEl.checked
          ? "Header: Authorization: Bearer pizza-staff-key"
          : "Header: (none — anonymous student)";
      }
    }

    function parseQuery(qs) {
      var out = {};
      if (!qs) return out;
      qs.split("&").forEach(function (pair) {
        var idx = pair.indexOf("=");
        if (idx === -1) return;
        var k = decodeURIComponent(pair.slice(0, idx)).trim();
        var val = decodeURIComponent(pair.slice(idx + 1)).trim();
        if (k) out[k] = val;
      });
      return out;
    }

    function handleRequest(method, rawPath, hasAuth, rawBody) {
      var clean = (rawPath || "").trim();
      if (!clean.startsWith("/")) clean = "/" + clean;
      var qIdx = clean.indexOf("?");
      var pathname = qIdx === -1 ? clean : clean.slice(0, qIdx);
      var query = parseQuery(qIdx === -1 ? "" : clean.slice(qIdx + 1));
      pathname = pathname.replace(/\/+$/, "") || "/";

      lastHighlight = { table: null, id: null };

      // GET /v1/menu
      if (method === "GET" && pathname === "/v1/menu") {
        var items = state.menu.slice();
        if (query.category) {
          items = items.filter(function (m) {
            return m.category.toLowerCase() === query.category.toLowerCase();
          });
        }
        if (query.maxPrice) {
          var maxP = Number(query.maxPrice);
          if (!isNaN(maxP)) {
            items = items.filter(function (m) { return m.price <= maxP; });
          }
        }
        return { status: 200, text: "200 OK", body: { count: items.length, items: items } };
      }

      // /v1/menu/:id
      var menuMatch = pathname.match(/^\/v1\/menu\/(\d+)$/);
      if (menuMatch) {
        var mid = parseInt(menuMatch[1], 10);
        var mIdx = state.menu.findIndex(function (m) { return m.id === mid; });
        if (method === "GET") {
          if (mIdx === -1) {
            return { status: 404, text: "404 Not Found", body: { error: "Menu item " + mid + " not found." } };
          }
          return { status: 200, text: "200 OK", body: state.menu[mIdx] };
        }
        if (method === "DELETE") {
          if (!hasAuth) {
            return {
              status: 401,
              text: "401 Unauthorized",
              body: {
                error: "Staff API key required to edit or delete the menu.",
                hint: "Turn on the Staff API Key toggle (Authorization: Bearer ...) and retry."
              }
            };
          }
          if (mIdx === -1) {
            return { status: 404, text: "404 Not Found", body: { error: "Menu item " + mid + " not found." } };
          }
          var removedMenu = state.menu.splice(mIdx, 1)[0];
          return { status: 200, text: "200 OK", body: { deleted: removedMenu } };
        }
        return { status: 405, text: "405 Method Not Allowed", body: { error: method + " is not allowed on " + pathname } };
      }

      // /v1/orders
      if (pathname === "/v1/orders") {
        if (method === "GET") {
          return { status: 200, text: "200 OK", body: { count: state.orders.length, items: state.orders } };
        }
        if (method === "POST") {
          var parsed;
          try {
            parsed = JSON.parse(rawBody || "");
          } catch (err) {
            return {
              status: 400,
              text: "400 Bad Request",
              body: { error: "Invalid JSON body. Check double quotes and commas." }
            };
          }
          if (!parsed || !parsed.item || !parsed.customer) {
            return {
              status: 400,
              text: "400 Bad Request",
              body: { error: "Missing required fields: both 'customer' and 'item' are required." }
            };
          }
          var created = {
            id: state.nextOrderId++,
            customer: String(parsed.customer).slice(0, 30),
            item: String(parsed.item).slice(0, 30),
            status: "preparing"
          };
          state.orders.push(created);
          lastHighlight = { table: "orders", id: created.id };
          return { status: 201, text: "201 Created", body: created };
        }
        return { status: 405, text: "405 Method Not Allowed", body: { error: method + " is not allowed on /v1/orders" } };
      }

      // /v1/orders/:id
      var orderMatch = pathname.match(/^\/v1\/orders\/(\d+)$/);
      if (orderMatch) {
        var oid = parseInt(orderMatch[1], 10);
        var oIdx = state.orders.findIndex(function (o) { return o.id === oid; });
        if (method === "GET") {
          if (oIdx === -1) {
            return { status: 404, text: "404 Not Found", body: { error: "Order #" + oid + " does not exist." } };
          }
          return { status: 200, text: "200 OK", body: state.orders[oIdx] };
        }
        if (method === "PATCH" || method === "PUT") {
          if (oIdx === -1) {
            return { status: 404, text: "404 Not Found", body: { error: "Order #" + oid + " does not exist." } };
          }
          var patch;
          try {
            patch = JSON.parse(rawBody || "");
          } catch (err) {
            return { status: 400, text: "400 Bad Request", body: { error: "Invalid JSON body." } };
          }
          if (method === "PUT" && (!patch.customer || !patch.item || !patch.status)) {
            return {
              status: 400,
              text: "400 Bad Request",
              body: { error: "PUT replaces the whole order: provide customer, item, and status (or use PATCH to edit one field)." }
            };
          }
          if (patch.customer) state.orders[oIdx].customer = String(patch.customer).slice(0, 30);
          if (patch.item) state.orders[oIdx].item = String(patch.item).slice(0, 30);
          if (patch.status) state.orders[oIdx].status = String(patch.status).slice(0, 20);
          lastHighlight = { table: "orders", id: oid };
          return { status: 200, text: "200 OK", body: state.orders[oIdx] };
        }
        if (method === "DELETE") {
          if (!hasAuth) {
            return {
              status: 401,
              text: "401 Unauthorized",
              body: { error: "Staff API key required to cancel orders.", hint: "Turn on the Staff API Key toggle and retry." }
            };
          }
          if (oIdx === -1) {
            return { status: 404, text: "404 Not Found", body: { error: "Order #" + oid + " does not exist." } };
          }
          var removedOrder = state.orders.splice(oIdx, 1)[0];
          return { status: 200, text: "200 OK", body: { cancelled: removedOrder } };
        }
      }

      return {
        status: 404,
        text: "404 Not Found",
        body: {
          error: "No route matches " + method + " " + pathname,
          hint: "Try /v1/menu, /v1/menu?category=pizza, /v1/orders, or /v1/orders/101"
        }
      };
    }

    function sendCurrent() {
      var res = handleRequest(verbEl.value, pathEl.value, !!(authEl && authEl.checked), bodyEl ? bodyEl.value : "");
      if (statusEl) {
        statusEl.textContent = res.text;
        statusEl.className = "api-status " + (res.status < 300 ? "api-status--2xx" : "api-status--4xx");
      }
      if (metaEl) {
        metaEl.textContent = "Content-Type: application/json · 12 ms (local)";
      }
      if (resBodyEl) {
        resBodyEl.textContent = JSON.stringify(res.body, null, 2);
      }
      renderDb();
    }

    var PRESETS = {
      "list-menu": { verb: "GET", path: "/v1/menu", auth: false, body: "" },
      "place-order": {
        verb: "POST",
        path: "/v1/orders",
        auth: false,
        body: '{\n  "customer": "Kuba",\n  "item": "Pepperoni"\n}'
      },
      "hack-delete": { verb: "DELETE", path: "/v1/menu/2", auth: false, body: "" },
      "filter-pizza": { verb: "GET", path: "/v1/menu?category=pizza&maxPrice=30", auth: false, body: "" },
      "not-found": { verb: "GET", path: "/v1/orders/999", auth: false, body: "" }
    };

    Array.prototype.slice.call(root.querySelectorAll("[data-pg-preset]")).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var preset = PRESETS[btn.getAttribute("data-pg-preset")];
        if (!preset) return;
        verbEl.value = preset.verb;
        pathEl.value = preset.path;
        if (authEl) authEl.checked = preset.auth;
        if (bodyEl && preset.body) bodyEl.value = preset.body;
        syncControls();
        sendCurrent();
      });
    });

    verbEl.addEventListener("change", syncControls);
    if (authEl) authEl.addEventListener("change", syncControls);
    sendBtn.addEventListener("click", sendCurrent);
    pathEl.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        sendCurrent();
      }
    });

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        seedState();
        verbEl.value = "GET";
        pathEl.value = "/v1/menu";
        if (authEl) authEl.checked = false;
        syncControls();
        if (statusEl) {
          statusEl.textContent = "Ready";
          statusEl.className = "api-status api-status--idle";
        }
        if (metaEl) metaEl.textContent = "Pick a preset or click Send";
        if (resBodyEl) resBodyEl.textContent = "// Database reset! Click 'Send' or try a quick demo button above.";
        renderDb();
      });
    }

    seedState();
    syncControls();
    renderDb();
  }

  /* =========================================================================
     4. GOOD VS BAD DESIGN FLIP CARDS (Beat 6)
     ========================================================================= */
  function initFlipCards(root) {
    var cards = Array.prototype.slice.call(root.querySelectorAll(".api-flip"));
    if (!cards.length) return;

    cards.forEach(function (card) {
      var btn = card.querySelector(".api-flip-toggle");
      if (!btn) return;
      btn.addEventListener("click", function () {
        var revealed = card.classList.toggle("is-revealed");
        btn.textContent = revealed ? "Hide fix" : "Reveal clean fix";
      });
    });

    var revealAll = document.getElementById("api-flip-all");
    if (revealAll) {
      revealAll.addEventListener("click", function () {
        var allOpen = cards.every(function (c) { return c.classList.contains("is-revealed"); });
        cards.forEach(function (card) {
          card.classList.toggle("is-revealed", !allOpen);
          var btn = card.querySelector(".api-flip-toggle");
          if (btn) btn.textContent = !allOpen ? "Hide fix" : "Reveal clean fix";
        });
        revealAll.textContent = !allOpen ? "Hide all fixes" : "Reveal all fixes";
      });
    }
  }

  /* =========================================================================
     5. CODE REVIEW THIS BAD API CHALLENGE (Beat 8)
     ========================================================================= */
  function initCodeReviewQuiz(root) {
    var qcards = Array.prototype.slice.call(root.querySelectorAll(".api-qcard"));
    var scoreEl = document.getElementById("api-quiz-score");
    var resetBtn = document.getElementById("api-quiz-reset");
    if (!qcards.length) return;

    var answered = {};

    function updateScore() {
      var right = 0;
      Object.keys(answered).forEach(function (k) {
        if (answered[k]) right += 1;
      });
      if (scoreEl) {
        scoreEl.textContent = "Score: " + right + " / " + qcards.length;
      }
    }

    qcards.forEach(function (card, qIdx) {
      var opts = Array.prototype.slice.call(card.querySelectorAll(".api-qopt"));
      var fb = card.querySelector(".api-qcard__fb");
      var reason = card.getAttribute("data-reason") || "";

      opts.forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (qIdx in answered) return;
          var isCorrect = btn.getAttribute("data-correct") === "1";
          answered[qIdx] = isCorrect;

          opts.forEach(function (o) {
            o.disabled = true;
            if (o.getAttribute("data-correct") === "1") {
              o.classList.add("is-right");
            }
          });
          if (!isCorrect) btn.classList.add("is-wrong");

          if (fb) {
            fb.className = "api-qcard__fb " + (isCorrect ? "is-right" : "is-wrong");
            fb.textContent = (isCorrect ? "Spot on! " : "Not quite. ") + reason;
          }
          updateScore();
        });
      });
    });

    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        answered = {};
        qcards.forEach(function (card) {
          var fb = card.querySelector(".api-qcard__fb");
          if (fb) {
            fb.className = "api-qcard__fb";
            fb.textContent = "";
          }
          Array.prototype.slice.call(card.querySelectorAll(".api-qopt")).forEach(function (o) {
            o.disabled = false;
            o.classList.remove("is-right", "is-wrong");
          });
        });
        updateScore();
      });
    }

    updateScore();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
