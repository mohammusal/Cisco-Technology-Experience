"""Parse every Mermaid diagram in the built site with the bundled mermaid.min.js.

Run after `mkdocs build`. Uses headless Microsoft Edge (or set EDGE to a Chromium binary).
"""

import html
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
EDGE = os.environ.get("EDGE", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


def collect():
    diagrams = []
    for page in sorted(SITE.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        for match in re.finditer(r'<pre class="mermaid"[^>]*><code>(.*?)</code></pre>', text, re.S):
            diagrams.append((page.relative_to(SITE).as_posix(), html.unescape(match.group(1))))
    return diagrams


def main():
    diagrams = collect()
    mermaid_js = (SITE / "assets/javascripts/mermaid.min.js").as_uri()
    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "check.html"
        page.write_text(f"""<!doctype html><meta charset="utf-8">
<script src="{mermaid_js}"></script>
<pre id="out">pending</pre>
<script>
const items = {json.dumps(diagrams)};
mermaid.initialize({{startOnLoad: false}});
(async () => {{
  const lines = [];
  for (const [page, src] of items) {{
    try {{ await mermaid.parse(src); }}
    catch (e) {{
      lines.push("FAIL " + page + " :: " + src.split("\\n").slice(0, 2).join(" | ")
                 + " :: " + String(e.message || e).slice(0, 300));
    }}
  }}
  lines.push("DONE " + items.length);
  document.getElementById("out").textContent = lines.join("\\n");
}})();
</script>""", encoding="utf-8")
        result = subprocess.run(
            [EDGE, "--headless=new", "--disable-gpu", f"--user-data-dir={tmp}/profile",
             "--allow-file-access-from-files", "--virtual-time-budget=15000",
             "--dump-dom", page.as_uri()],
            capture_output=True, text=True, encoding="utf-8", timeout=120,
        )
    found = re.search(r'<pre id="out">(.*?)</pre>', result.stdout, re.S)
    output = html.unescape(found.group(1)) if found else result.stdout[-500:]
    report = [line for line in output.splitlines() if line.startswith(("FAIL", "DONE"))]
    print("\n".join(report) or "no result: " + output)
    if not any(line.startswith("DONE") for line in report) or any(l.startswith("FAIL") for l in report):
        sys.exit(1)


if __name__ == "__main__":
    main()
