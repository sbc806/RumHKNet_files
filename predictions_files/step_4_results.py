import os as os
import pandas as pd
import numpy as np

predictions_path="../../predictions/predicted_results/step_4/both/clustered"

small_dir_0_path=os.path.join(predictions_path,"small_histidine_kinase_batch_0")
for f in os.listdir(small_dir_0_path):
  df=pd.read_csv(os.path.join(small_dir_0_path,f))

small_df=pd.concat(small_dfs)
predictions_information(complete_small_df)

complete_large_df=pd.read_csv(os.path.join(predictions_path,"clustered_rep_seq95_large_histidine_kinase_batch_predicted_03.csv"))
predictions_information(complete_large_df)

print("newrun_seqs")
complete_large_df=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_histidine_kinase_batch_predicted_03.csv"))
predictions_information(complete_large_df)
