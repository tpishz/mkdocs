"""
Deals with generating the per-page table of contents.

For the sake of simplicity we use the Python-Markdown `toc` extension to
generate a list of dicts for each toc item, and then store it as AnchorLinks to
maintain compatibility with older versions of MkDocs.
"""
from typing import List


def get_toc(toc_tokens):
    toc = [_parse_toc_token(i) for i in toc_tokens]
    # For the table of contents, always mark the first element as active
    if len(toc):
        toc[0].active = True
    return TableOfContents(toc)


class TableOfContents:
    """
    Represents the table of contents for a given page.
    """

    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ''.join([str(item) for item in self])


class AnchorLink:
    """
    A single entry in the table of contents.
    """

    def __init__(self, title: str, id: str, level: int):
        self.title, self.id, self.level = title, id, level
        self.children = []

    title: str
    """The text of the item."""

    @property
    def url(self) -> str:
        """The hash fragment of a URL pointing to the item."""
        return '#' + self.id

    level: int
    """The zero-based level of the item."""

    children: List['AnchorLink']
    """An iterable of any child items."""

    def __str__(self):
        return self.indent_print()

    def indent_print(self, depth=0):
        indent = '    ' * depth
        ret = f'{indent}{self.title} - {self.url}\n'
        for item in self.children:
            ret += item.indent_print(depth + 1)
        return ret


def _parse_toc_token(token):
    anchor = AnchorLink(token['name'], token['id'], token['level'])
    for i in token['children']:
        anchor.children.append(_parse_toc_token(i))
    return anchor
