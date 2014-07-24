from __future__ import print_function, unicode_literals
from .schema import SCHEMA
from whoosh import index
import os
import sys
from conceptnet5.formats.json_stream import read_json_stream


def index_assertions(input_dir, output_dir):
    filenames = sorted(os.listdir(input_dir))
    ix = index.create_in(output_dir, SCHEMA)
    for filename in filenames:
        if filename.endswith('.jsons'):
            writer = ix.writer()
            path = os.path.join(input_dir, filename)
            print("\tIndexing %s" % filename, end='')
            sys.stdout.flush()
            count = 0
            for a, offset in read_json_stream(path, offsets=True):
                writer.add_document(
                    rel=a['rel'],
                    start=a['start'],
                    end=a['end'],
                    dataset=a['dataset'],
                    sources=' '.join(a['sources']),
                    filename=filename,
                    offset=offset
                )
                count += 1
                if count % 10000 == 0:
                    print('.', end='')
                    sys.stdout.flush()
            print()
            writer.commit()
