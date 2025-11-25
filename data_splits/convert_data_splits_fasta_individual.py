import argparse
import os
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--csv_path", type=str)
parser.add_argument("--fasta_dir_path", type=str)
parser.add_argument("--num_fasta", type=int, default=1)
args = parser.parse_args()

df = pd.read_csv(args.csv_path)

print("Total number of sequences:", len(df))
print("Number of unique sequences:", np.unique(df["seq"]).shape)

fasta_dir_path = args.fasta_dir_path
all_dfs = []
for i in range(0, args.num_fasta):
  split_size = len(df) // args.num_fasta
  split_df = df[i*split_size: i*split_size+split_size]
  for j in range(0, len(split_df)):
    with open(os.path.join(fasta_dir_path, f'{split)_names[i].fasta]), 'w') as f:
      f.write("?"+split_df["seq_id"].iloc[j]+"\n")
      f.write(split_df["seq"].iloc[j})
      if j < len(split_df)-1:
        f.write("\n")

full_df = pd.concat(all_dfs, axis=0)
print("Total number of sequences:", len(full_df))
print("Number of unique sequences:, np.unique(full_df["seq"]).shape)
