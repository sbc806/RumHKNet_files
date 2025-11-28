import numpy as np
import os as os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
predictions_dir=os.path.join(dir_path,"predictions/predicted_results/step_1")
prediction_csv=os.listdir(predictions_dir)
prediction_csv_filtered=[ f for f in prediction_csv if "five_sequences" not in f]
threshold_files={}
for f in prediction_csv_filtered:
  threshold=f.split(".csv")[0].split("_")[-1]
  print(threshold)
  if threshold in threshold_files:
    threshold_files[threshold].append(f)
  else:
    threshold_files[threshold]=[f]

for threshold in threshold_files:
  threshold_files[threshold]=sorted(threshold_files[threshold])

def stack_csvs(files):
  dfs=[]
  for f in files:
    df=pd.read_csv(f)
    dfs.append(df)
  return pd.concat(dfs)
df_07=stack_csvs(threshold_files["07"])
print("Number of examples:",len(df_07))
split_dir_path=os.path.join(dir_path,"sbc806/RumHKNet/kinases_dataset/step_1_non_kinases_preprocessed/protein/binary_class")
train_path=os.path.join(split_dir_path,"train/train.csv")
train_df=pd.read_csv(train_path)
print("Number of xamples in training set:",len(train_df))
print("Number of common rows:",np.sum(train_df["seq_id"]==df_07["seq_id"]))
