import os as os
import numpy as np
import pandas as pd

def check_specific(dir_path,f_name):
  files=os.listdir(dir_path)
  selected_files=[f for f in files if f_name in f]

  dfs=[]
  for f in selected_files:
    df=pd.read_csv(os.path.join(dir_path,f))
    print(f,len(df))
    dfs.append(df)
  return pd.concat(dfs)

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1_step_2_combined/both/clustered"

ko=check_specific(dir_path,"histidine_ko_no_blastp_no_rumhknet")
blastp=check_specific(dir_path,"histidine_blastp_ko_no_rumhknet")

print("KO:",len(ko))
print("Blastp:",len(blastp))
