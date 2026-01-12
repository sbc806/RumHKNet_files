import numpy as np
import pandas as pd
import os as os

predictions_path="../../predictions/predicted_results/step_1/both/clustered"
df_1=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_0_predicted_03.csv"))
df_2=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_1_predicted_03.csv"))
df=pd.concat([df_1,df_2])
print(np.unique(df["seq"]).shape)
print(np.unique(df["seq_id"]).shape)
length=df["seq"].str.len()>=12211
print(np.sum(length))
