import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific

dataset_path= "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

i_df={}
small=[]
small_total=0
for i in range(0,7):
  df=check_specific(predictions_path,f"2026_04_22_clustered95_rep_seq_small_{i}_")
  print(i,len(df))
  small_total=small_total+len(df)
print(small_total)

large=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_large_predicted_02_v2.csv"))
print("Number of predictions for sequences with length >1500:",len(large))
