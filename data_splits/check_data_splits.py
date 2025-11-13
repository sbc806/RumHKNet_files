import argparse
import os
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--dir_path", type=str)
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

split_dfs = [train_df, dev_df, test_df]
split_names = ["train", "dev", "test"]
for i, each_df in enumerate(split_dfs):
  print(f"Number of samples in {split_names[i]}: {len(each_df)}")
  labels = each_df["label"]
  print(f"Labels for {split_names[i]}: {np.unique(labels)}")
  if "batch" in each_df.columns:
    batches = each_df["batch"]
    print(f"Batches for {split_names[i]}: {np.unique(batches)}")


