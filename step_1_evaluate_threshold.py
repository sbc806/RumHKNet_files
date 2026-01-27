import numpy as np
import os as os
import pandas as pd
import re

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
predictions_dir_path=os.path.join(dir_path,"predictions/predicted_results/step_1/both")
prediction_csv=os.listdir(predictions_dir_path)
"""
prediction_csv_filtered=[ f for f in prediction_csv if "five_sequences" not in f]
threshold_files={}
for f in prediction_csv_filtered:
  threshold=f.split(".csv")[0].split("_")[-1]
  print(threshold)
  if threshold in threshold_files:
    threshold_files[threshold].append(os.path.join(predictions_dir_path,f))
  else:
    threshold_files[threshold]=[os.path.join(predictions_dir_path,f)]

for threshold in threshold_files:
  threshold_files[threshold]=sorted(threshold_files[threshold])
"""
print("Training accuracy")
thresholds=["02","05","07"]
threshold_files={}
for threshold in thresholds:
  threshold_f=[]
  for f in prediction_csv:
    if re.search(rf"train_\d_predicted_{threshold}.csv"):
      threshold_f.append(os.path.join(predictions_dir_path,f))
  threhsold_files[threshold]=sorted(threshold_f)
  print(threshold,threshold_files[threshold])
  
def stack_csvs(files):
  dfs=[]
  for f in files:
    df=pd.read_csv(f)
    dfs.append(df)
  return pd.concat(dfs)
df_07=stack_csvs(threshold_files["07"])
df_07=df_07.reset_index(drop=True)
print("Number of examples:",len(df_07))
print(df_07)
split_dir_path=os.path.join(dir_path,"sbc806/RumHKNet/kinases_dataset/step_1_non_kinases_preprocessed/protein/binary_class")
train_path=os.path.join(split_dir_path,"train/train.csv")
train_df=pd.read_csv(train_path)
print("Number of xamples in training set:",len(train_df))
print(train_df)
print("Number of common rows:",np.sum(train_df["seq_id"]==df_07["seq_id"]))

thresholds=[0.2,0.25,0.3,0.35,0.4,0.5,0.7,0.9]
for threshold in thresholds:
  predictions=df_07["prob"]>=threshold
  labels=train_df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy)

print("Validation accuracy")
step_1_dev_df=pd.read_csv(os.path.join(dir_path,"kinases_dataset/step_1_non_kinases_preprocessed/protein/binary_class/dev/dev.csv"))
step_1_non_kinases_preprocessed_dev_predicted_df=pd.read_csv(os.path.join(predictions_dir_path,"step_1_non_kinases_preprocessed_dev_predicted_03_v2.csv"))
for threshold in thresholds:
  predictions=step_1_non_kinases_preprocessed_dev_predicted_df["prob"]>=threshold
  labels=step_1_dev_df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy)
  
