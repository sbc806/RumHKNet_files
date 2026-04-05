import os
import pandas as pd
import numpy as np

dataset_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

i_df={}
for i in range(0,5):
  df_i=get_select(predictions_path,"newadd_155098MAGs_small_{i}")
  print(len(df_i))
  i_df[i]=df_i
large_df=pd.read_csv(os.path.join("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/newadd_155098MAGs_large_predicted_02_v2.csv"))
