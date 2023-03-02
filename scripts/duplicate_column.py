import pandas as pd
import re
import sys

#This just adds the correct sequence length, without - or N, for those that were actually
#used in the analysis (passed 'filter') to the metadata

if __name__ == '__main__':
    import argparse

    parser = parser = argparse.ArgumentParser(description='Duplicate column',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--meta-in', help="input meta file")
    parser.add_argument('--meta-out', help="output metadata with duplicated column")
    parser.add_argument('--column-to-dup', help="column to duplicate")
    parser.add_argument('--dup-column-name', help="name of new column")     
    args = parser.parse_args()

    orig_meta = args.meta_in #"results/metadata-ages.tsv"
    meta = pd.read_csv(orig_meta, sep='\t', index_col=False)

    if args.column_to_dup not in meta:
        sys.exit(f"Column '{args.column_to_dup}' isn't found in the metadata. Please use a column that's present. \nExiting.")

    if args.dup_column_name in meta:
        sys.exit(f"New column name '{args.dup_column_name}' is already in use. Use a different new column name. \nExiting.")

    meta[args.dup_column_name] = meta.loc[:, args.column_to_dup]

    meta.to_csv(args.meta_out, sep="\t", index=False)
