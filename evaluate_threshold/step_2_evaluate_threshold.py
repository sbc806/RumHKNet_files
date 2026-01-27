import numpy as np
import os as os
import pandas as pd
import re
from sklearn.metrics import precision_score, recall_score

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
predictions_dir_path=os.path.join(dir_path,"predictions/predicted_results/step_2/both")
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
threshold_files={}
thresholds=["02","035","05","07","09"]
for threshold in thresholds:
  threshold_f=[]
  for f in prediction_csv:
    pattern=rf"train_\d_predicted_{threshold}.csv"
    if re.search(pattern,f):
      threshold_f.append(os.path.join(predictions_dir_path,f))
  threshold_files[threshold]=sorted(threshold_f)
  print(threshold,threshold_files[threshold])
def stack_csvs(files):
  dfs=[]
  for f in files:
    df=pd.read_csv(f)
    dfs.append(df)
  return pd.concat(dfs)
# threshold_df={}
# for threshold in threshold_files:
  # threshold_df[threshold]=stack_csvs(threshold_files[threshold]).reset_index(drop=True)
"""
df_07=stack_csvs(threshold_files["07"])
df_07=df_07.reset_index(drop=True)
print("Number of examples:",len(df_07))
print(df_07)
"""

split_dir_path=os.path.join(dir_path,"kinases_dataset/extra_p_2_class_v3_kinases_only/protein/binary_class")
train_path=os.path.join(split_dir_path,"train/train.csv")
train_df=pd.read_csv(train_path)
"""
labels=train_df["label"]
print("Number of examples in training set:",len(train_df))
print(train_df)
for threshold in threshold_df:
  df=threshold_df[threshold]
  print("Number of common rows:",np.sum(train_df["seq_id"]==df["seq_id"]))
  predictions=df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy,"Correct:",correct,"Total:",total)
"""

# print("Training accuracy")
df_02=stack_csvs(threshold_files["02"])
df_02=df_02.reset_index(drop=True)
df_035=stack_csvs(threshold_files["035"])
df_035=df_035.reset_index(drop=True)
df_05=stack_csvs(threshold_files["05"])
df_05=df_05.reset_index(drop=True)
df_07=stack_csvs(threshold_files["07"])
df_07=df_07.reset_index(drop=True)
df_09=stack_csvs(threshold_files["09"])
df_0=df_09.reset_index(drop=True)
print(len(df_02),len(df_035),len(df_05),len(df_07),len(df_09))
print()
print("Training accuracy")
print(df_02)
print(train_df)
print("Number of examples in training set:",len(train_df))
print("Number of examples in common:",np.sum(train_df["seq_id"]==df_02["seq_id"]))
thresholds=[0.2,0.3,0.35,0.4,0.5,0.7,0.9]
for threshold in thresholds:
  predictions=df_02["prob"]>=threshold
  labels=train_df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy)
print()
"""
print("Validation accuracy")
step_2_dev_df=pd.read_csv(os.path.join(dir_path,"kinases_dataset/extra_p_2_class_v3_kinases_only/protein/binary_class/dev/dev.csv"))
step_2_dev_predicted_df=pd.read_csv(os.path.join(predictions_dir_path,"extra_p_2_class_v3_kinases_only_dev_predicted_03_v2.csv"))
print(step_2_dev_predicted_df)
print(step_2_dev_df)
print("Number of examples in validation set:",len(step_2_dev_df))
print("Number of examples in common:",np.sum(step_2_dev_df["seq_id"]==step_2_dev_predicted_df["seq_id"]))
for threshold in thresholds:
  predictions=step_2_dev_predicted_df["prob"]>=threshold
  labels=step_2_dev_df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy,"Precision:",precision_score(labels.values,predictions.values),"Recall:",recall_score(labels.values,predictions.values))
"""
