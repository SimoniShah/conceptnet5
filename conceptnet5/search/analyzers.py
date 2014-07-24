from __future__ import unicode_literals
from whoosh.analysis.tokenizers import Tokenizer
from whoosh.analysis.filters import LowercaseFilter
from whoosh.analysis.acore import Token
from conceptnet5.uri import uri_prefixes, split_uri, concept_uri


class URITokenizer(Tokenizer):
    def __init__(self, min_pieces=2):
        self.min_pieces = min_pieces

    def __call__(self, value, **kwargs):
        token = Token()
        for uri in value.split(' '):
            if uri.startswith('/'):
                # temporary workaround for malformed sources
                for prefix in uri_prefixes(uri):
                    token.text = prefix
                    yield token


def URIAnalyzer():
    return URITokenizer() | LowercaseFilter()


class SurfaceTextTokenizer(Tokenizer):
    def __call__(self, value):
        token = Token()
        for uri in value.split(' '):
            uri_pieces = split_uri(uri)
            language = uri_pieces[1]
            lemmas = uri_pieces[2].split('_')
            for lemma in lemmas:
                token.text = concept_uri(language, lemma)
                yield token


def SurfaceTextAnalyzer():
    return SurfaceTextTokenizer()
