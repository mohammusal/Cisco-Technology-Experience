"""Build the Glossary page from docs/includes/abbreviations.md.

The same file feeds the hover tooltips on every page, so the page and the
tooltips always agree. Plural entries are left out of the page.
"""

import re
from pathlib import Path

MARKER = "<!-- glossary-terms -->"
ENTRY = re.compile(r"^\*\[(?P<term>[^\]]+)\]:\s*(?P<text>.+)$")
PLURALS = {
    "programs", "variables", "strings", "operators", "loops", "lists",
    "tuples", "dictionaries", "functions", "exceptions", "parameters",
    "arguments",
}


def _terms(docs_dir):
    source = Path(docs_dir) / "includes" / "abbreviations.md"
    for line in source.read_text(encoding="utf-8").splitlines():
        match = ENTRY.match(line.strip())
        if match and match["term"] not in PLURALS:
            yield match["term"], match["text"]


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown
    terms = sorted(_terms(config["docs_dir"]), key=lambda item: item[0].lower())
    rows = "\n\n".join(f"`{term}`\n:   {text}" for term, text in terms)
    return markdown.replace(MARKER, rows)
