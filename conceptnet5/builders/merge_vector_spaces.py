from assoc_space import AssocSpace
import argparse
import os


def merge_n_vector_spaces(subspace_dir, output_dir, k=300):
    spaces = []
    for subdir in os.listdir(subspace_dir):
        if subdir.startswith('part_'):
            path = os.path.join(subspace_dir, subdir)
            spaces.append(AssocSpace.load_dir(path))

    merged = AssocSpace.merge_many(spaces, k=k)
    merged.save_dir(output_dir)
    return merged


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')

    args = parser.parse_args()
    merge_n_vector_spaces(args.input_dir, args.output_dir)
