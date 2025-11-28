import numpy as np
import os as os
import pandas as pd

dir_path="/home/schen123/scratch/kinases"
predictions_dir_path=os.path.join(dir_path,"predictions/predicted_results/step_2/both")
prediction_csv=os.listdir(predictions_dir_path)
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

def stack_csvs(files):
  dfs=[]
  for f in files:
    df=pd.read_csv(f)
    dfs.append(df)
  return pd.concat(dfs)
threshold_df={}
for threshold in threshold_files:
  threshold_df[threshold]=stack_csvs(threshold_files[threshold])
"""
df_07=stack_csvs(threshold_files["07"])
df_07=df_07.reset_index(drop=True)
print("Number of examples:",len(df_07))
print(df_07)
"""
split_dir_path=os.path.join(dir_path,"sbc806/RumHKNet/kinases_dataset/extra_p_2_class_v133/protein/multi_class")
train_path=os.path.join(split_dir_path,"train/train.csv")
train_df=pd.read_csv(train_path)
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
thresholds=[0.2,0.35,0.5,0.7,0.9]
for threshold in thresholds:
  predictions=df_07["prob"]>=threshold
  labels=train_df["label"]
  correct=np.sum(predictions==labels)
  total=len(labels)
  accuracy=correct/total
  print("Threshold:",threshold,"Accuracy:",accuracy)
"""
