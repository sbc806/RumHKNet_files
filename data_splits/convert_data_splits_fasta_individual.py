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
split_dfs = [train_df, dev_df, test_df, full_df]
split_names = ["train", "dev", "test", "full"]
for i, each_df in enumerate(split_dfs):
  with open(os.path.join(fasta_dir_path, f'{split_names[i]}.fasta'), 'w') as f:
    for j in range(0, len(each_df)):
      f.write(">"+each_df["seq_id"].iloc[j]+"\n")
      f.write(each_df["seq"].iloc[j])
      if j < len(each_df)-1:
        f.write("\n")
