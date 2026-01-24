import os as os
import pandas as pd
import numpy as np

step_1_rbag_02_df=pd.read_csv("../../predictions/predictions_dataset/step_2/clustered/step_1_clustered_newrun_rbags_02_not_contained.csv")
split_size=900000
num_splits=len(step_1_rbag_02_df)//split_size
for i in range(0,len(num_splits)):
  start=i*split_size
  end=start+split_size
  step_1_rbag_02_df_i=step_1_rbag_02_df[start:end]
  step_1_rbag_02_df_i.to_csv(f"../../predictions/predictions_dataset/step_2/clustered/step_1_clustered_newrun_rbags_02_not_contained_{i}.csv",index=False)


