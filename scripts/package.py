"""Build the offline student handout: dist/python-workshop.zip.

    python scripts/package.py

Steps:
1. mkdocs build --strict           -> site/
2. assemble dist/python-workshop/
       START_HERE.html  (opens guide/index.html)
       guide/           (the built site)
       code/            (starter files and solutions, without generated files)
3. fail if any HTML or CSS file loads a resource from the internet
4. zip it to dist/python-workshop.zip
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DIST = ROOT / "dist"
NAME = "python-workshop"
BUNDLE = DIST / NAME

# Files students create while working; they must not be in the handout.
SKIP_IN_CODE = shutil.ignore_patterns(
    ".venv", "__pycache__", "*.pyc", "scores.txt", "notes.txt", "temperatures.txt", ".DS_Store"
)

START_HERE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=guide/index.html">
<title>Python Workshop</title>
</head>
<body>
<p><a href="guide/index.html">Open the Python Workshop guide</a></p>
</body>
</html>
"""

# Things that make the browser download something: src=, <link href=>, CSS url(), @import.
# Plain <a href="https://..."> links are fine: they only open when clicked.
RESOURCE_PATTERNS = [
    re.compile(r"""\bsrc\s*=\s*["']?(?P<url>(?:https?:)?//[^"'\s>]+)""", re.I),
    re.compile(r"""url\(\s*["']?(?P<url>(?:https?:)?//[^"')\s]+)""", re.I),
    re.compile(r"""@import\s+["'](?P<url>(?:https?:)?//[^"']+)""", re.I),
]
LINK_TAG = re.compile(r"<link\b[^>]*>", re.I)
LINK_HREF = re.compile(r"""\bhref\s*=\s*["']?(?P<url>(?:https?:)?//[^"'\s>]+)""", re.I)
# Browsers never download these: they only name the page's address on the hosted site.
NOT_DOWNLOADED = re.compile(r"""\brel\s*=\s*["']?(?:canonical|alternate)\b""", re.I)
ALLOWED = (
    "http://www.w3.org/",  # SVG and XML namespaces, never downloaded
    "https://www.w3.org/",
)


def build_site():
    print("1/4 Building the site (mkdocs build --strict) ...")
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean"], cwd=ROOT
    )
    if result.returncode != 0:
        sys.exit("mkdocs build --strict failed: fix the warnings above first.")


def assemble():
    print(f"2/4 Assembling {BUNDLE.relative_to(ROOT)} ...")
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir(parents=True)
    shutil.copytree(SITE, BUNDLE / "guide")
    shutil.copytree(ROOT / "code", BUNDLE / "code", ignore=SKIP_IN_CODE)
    (BUNDLE / "START_HERE.html").write_text(START_HERE, encoding="utf-8")


def find_external_resources():
    print("3/4 Checking that nothing is loaded from the internet ...")
    found = []
    for path in sorted((BUNDLE / "guide").rglob("*")):
        if path.suffix not in (".html", ".css", ".js"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        urls = [m.group("url") for pattern in RESOURCE_PATTERNS for m in pattern.finditer(text)]
        for tag in LINK_TAG.finditer(text):
            href = LINK_HREF.search(tag.group(0))
            if href and not NOT_DOWNLOADED.search(tag.group(0)):
                urls.append(href.group("url"))
        found += [f"{path.relative_to(BUNDLE)}: {url}" for url in urls if not url.startswith(ALLOWED)]
    return found


def make_zip():
    print("4/4 Zipping ...")
    archive = shutil.make_archive(str(DIST / NAME), "zip", root_dir=DIST, base_dir=NAME)
    return Path(archive)


def main():
    sys.stdout.reconfigure(line_buffering=True)
    build_site()
    assemble()
    external = find_external_resources()
    if external:
        print(f"Found {len(external)} external resource URL(s):")
        for line in external:
            print("  " + line)
        sys.exit("The handout would not work offline.")
    print("   0 external resource URLs.")
    archive = make_zip()
    size_mb = archive.stat().st_size / 1_000_000
    print(f"Done: {archive.relative_to(ROOT)} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
