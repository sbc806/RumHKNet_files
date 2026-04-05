import os
import pandas as pd
import numpy as np
from ..predictions_helpers import check_specific


dataset_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

i_df={}
for i in range(0,5):
  df_i=check_specific(predictions_path,f"newadd_155098MAGs_small_{i}")
  print(len(df_i))
  i_df[i]=df_i
  
large_df=pd.read_csv(os.path.join("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/newadd_155098MAGs_large_predicted_02_v2.csv"))
print(len(large_df))
