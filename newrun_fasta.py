import os as os
import pandas as pd
from Bio import SeqIO

fasta_content=SeqIO.patse(open("../newrun_seqs.fasta"),'fasta')
seq_records=[]
for i, fasta in enumerate(fasta_content):
  name,sequence=fasta.id,str(fasta.seq)
  seq_record={"seq_id":name,"seq":sequence}
  seq_records.append(seq_record)

df=pd.DataFrame(seq_records)
print(df)
df.to_csv("../predictions/predictions_dataset/step_1/clustered/newrun_seqs.csv",index=False)
