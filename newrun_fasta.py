import numpy as np
import os as os
import pandas as pd
from Bio import SeqIO
"""
fasta_content=SeqIO.parse(open("../newrun_seqs.fasta"),'fasta')
seq_records=[]
for i, fasta in enumerate(fasta_content):
  name,sequence=fasta.id,str(fasta.seq)
  seq_record={"seq_id":name,"seq":sequence}
  seq_records.append(seq_record)

df=pd.DataFrame(seq_records)
"""
df=pd.read_csv("../predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv")
print(df)
df_1=df[df["seq"].str.len()<=1500]
df_2=df[df["seq"].str.len()>1500]
print(df_1)
print(df_2)
# sorted_1=np.argsort(df_1["seq"].str.len())
# sorted_2=np.argsort(df_2["seq"].str.len())
# sorted_df_1=df_1.iloc[sorted_1]
# sorted_df_2=df_2.iloc[sorted_2]
# print(sorted_df_1)
# print(sorted_df_2)
num_splits=len(df_1)//2450000+1
num_rows=0
for i in range(0,num_splits):
  start=i*num_splits
  end=i*num_splits+2450000
  df_subset=df_1[start:end]
  if end > len(df_1):
    end=len(df_1)
  num_rows=num_rows+len(df_subset)
  df_subset.to_csv(f"../predictions/predictions_dataset/step_1/clustered/newrun_seqs_small_{i}.csv",index=False)
print(num_rows)
df_2.to_csv(f"../predictions/predictions_dataset/step_1/clustered/newrun_seqs_large.csv",index=False)
print(max(df["seq"].str.len().values))
print(np.unique(df["seq"]).shape)
