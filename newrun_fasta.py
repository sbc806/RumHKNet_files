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
"""
num_splits=len(df)//2450000+1
num_rows=0
for i in range(0,num_splits):
  start=i*num_splits
  end=i*num_splits+2450000
  df_subset=df[start:end]
  num_rows=num_rows+len(df_subset)
  df_subset.to_csv(f"../predictions/predictions_dataset/step_1/clustered/newrun_seqs_{i}.csv",index=False)
print(num_rows)
"""
print(max(df["seq"].str.len().values))
print(np.unique(df["seq"]).shape)
