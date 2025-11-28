import os as os
import pandas as pd

dir="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
predictions_dir=os.path.join(dir_path,"predictions/predicted_results/step_1")
prediction_csv=os.lsitdir(predictions_dir)
predition_csv=[ f for f in prediction_csv if "five_sequences " not in f]

for f in prediction_csv_filtered:
  tehreshold=prediction_csv_filtered.split(".csv")[0].split("_")[-1]
  if threshold int rehshold_files:
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
