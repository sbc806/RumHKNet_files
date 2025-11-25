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
split_name = args.csv_path.split("/")[-1].split(".csv")[0]
fasta_dir_path = args.fasta_dir_path
all_dfs = []
split_size = len(df) //args.num_fasta
print("Split size:", split_size)
extension = ""
for i in range(0, args.num_fasta):
  split_df = df[i*split_size: i*split_size+split_size]
  if args.num_fasta > 1:
      extension = f"_{i}"
  for j in range(0, len(split_df)):
    with open(os.path.join(fasta_dir_path, f'{split_name}{extension}.fasta'), 'w') as f:
      f.write(">"+split_df["seq_id"].iloc[j]+"\n")
      f.write(split_df["seq"].iloc[j])
      if j < len(split_df)-1:
        f.write("\n")

full_df = pd.concat(all_dfs, axis=0)
print("Total number of sequences:", len(full_df))
print("Number of unique sequences:", np.unique(full_df["seq"]).shape)

small_df = df[0:5]
for i in range(0, len(small_df)):
  with open(os.path.join(fasta_dir_path, f'{split_name}_five_sequences.fasta'), 'w') as f:
    f.write(">"+small_df["seq_id"].iloc[i]+"\n")
    f.write(small_df["seq"].iloc[i])
    if i < len(split_df)-1:
      f.write("\n")
