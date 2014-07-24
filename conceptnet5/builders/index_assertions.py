from __future__ import unicode_literals
from conceptnet5.search.indexing import index_assertions
handle_file = index_assertions


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='directory of assertion files')
    parser.add_argument('output_dir', help='Whoosh index to output to')
    args = parser.parse_args()
    index_assertions(args.input_dir, args.output_dir)
