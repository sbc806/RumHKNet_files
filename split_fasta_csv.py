import os
import pandas as pd

csv_path = "../clustered_rep_seq95.csv"
df=pd.read_csv(csv_path)
split_size=2450000
df_large_seq=df[df["seq_length"]>1500].iloc[:,0:2]
df_small_seq=df[df["seq_length"]<=1500].iloc[:,0:2]
print(df_large_seq.shape,df_large_seq.columns)
print(df_small_seq.shape,df_small_seq.columns)

df_large_seq.to_csv("../clustered_rep_seq95_large.csv",index=False)

total_length=len(df_small_seq)//split_size+1
all_dfs=[]
for i in range(0,total_length)):
  start=i*split_size
  end=start+split_size
  selected_df=df_small_seq
  if i == total_length-1:
    selected_df=df_small_seq
  all_dfs.append(selected_df)
  selected_df.to_csv(f"../clustered_rep_seq95_small_{i}.csv",index=False)
