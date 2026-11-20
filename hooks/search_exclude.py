"""Keep Mermaid diagram source out of the search index.

The search plugin reads page.content in on_page_context, after this runs.
"""


def on_page_content(html, page, config, files):
    return html.replace('<pre class="mermaid">', '<pre class="mermaid" data-search-exclude>')
