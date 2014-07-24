from __future__ import unicode_literals
from whoosh import fields
from .analyzers import URIAnalyzer


SCHEMA = fields.Schema(
    uri=fields.ID(),
    rel=fields.TEXT(analyzer=URIAnalyzer(), phrase=False),
    start=fields.TEXT(analyzer=URIAnalyzer(), phrase=False),
    end=fields.TEXT(analyzer=URIAnalyzer(), phrase=False),
    dataset=fields.TEXT(analyzer=URIAnalyzer(), phrase=False),
    sources=fields.TEXT(analyzer=URIAnalyzer(), phrase=False),
    filename=fields.ID(stored=True),
    offset=fields.NUMERIC(stored=True)
)
