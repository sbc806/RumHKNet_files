import argparse
import os
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("dir_path", type=str)
parser.add_argument("fasta_dir_path", type=str)
args = parser.parse_args()

dir_path = args.dir_path
train_path = os.path.join(dir_path, "train/train.csv")
dev_path = os.path.join(dir_path, "dev/dev.csv")
test_path = os.path.join(dir_path, "test/test.csv")

train_df = pd.read_csv(train_path)
dev_df = pd.read_csv(dev_path)
test_df = pd.read_csv(test_path)

full_df = pd.concat((train_df, dev_df, test_df), axis=0)

print("Total number of sequences:", len(full_df))
print("Number of unique sequences:", np.unique(full_df["seq"]).shape)

fasta_dir_path = args.fasta_dir_path
split_dfs = [train_df, dev_df, test_df, full_df]
split_names = ["train", "dev", "test", "full"]
for i, each_df in enumerate(split_dfs):
  with open(os.path.join(fasta_dir_path, f'{split_names}.fasta'), 'w') as f:
    for j in range(0, len(each_df)):
      f.write(">"+each_df["seq_id"].iloc[j]+"\n")
      f.write(each_df["seq"].iloc[j])
      if j < len(each_df)-1:
        f.write("\n")
