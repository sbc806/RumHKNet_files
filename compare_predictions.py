import os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results"
result_names=["train_0_predicted_02.csv","train_0_10000_new_predicted_03_3432_v3.csv","train_0_100000_new_predicted_03_3432_v3.csv"]
dfs=[]
for f_name in result_names:
  dfs.append(pd.read_csv(os.path.join(dir_path,f_name)))

for i in range(0,10000):
  seq_id=dfs[0]["seq_id"].iloc[i]
  probs=[]
  preds=[]
  for j in range(0,len(dfs)):
    probs.append(dfs[j]["prob"].iloc[i])
    preds.append(dfs[j]["pred"].iloc[i])
  print(seq_id,probs,preds)
  print()
