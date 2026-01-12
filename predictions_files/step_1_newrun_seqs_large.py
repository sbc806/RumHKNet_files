import numpy as np
import pandas as pd
import os as os

dataset_path="../../predictions/predictions_dataset/step_1/clustered"
predictions_path="../../predictions/predicted_results/step_1/both/clustered"
df_1=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_0_predicted_03.csv"))
df_2=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_1_predicted_03.csv"))
df=pd.concat([df_1,df_2])
print(np.unique(df["seq"]).shape)
print(np.unique(df["seq_id"]).shape)
length=df["seq"].str.len()>=12211
print(np.sum(length))

df_12211=df[length].iloc[:,0:2]
print(df_12211)
# df_12211.to_csv(os.path.join(dataset_path,"newrun_seqs_large_12211.csv"),index=False)

df_1=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_0_predicted_03.csv"))
df_2=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_1_predicted_03.csv"))
df_12211=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_12211_predicted_03.csv"))
df_12211_not=df[~length]
df=pd.concat([df_12211,df_12211_not])
print(np.unique(df["seq"]).shape)
print(np.unique(df["seq_id"]).shape)
kinase_df=df[df.iloc[:,3]==1]
print(len(kinase_df))
