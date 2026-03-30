from Bio import SeqIO
import os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
fasta_path=os.path.join(dir_path,"newadd_155098MAGs.fasta"))
fasta_content=SeqIO.parse(open(dir_path),"fasta")
seq_data=[]
for i, fasta in enumerate(fasta_content):
  seq_id,seq=fasta.id,fasta.seq
  seq_data.append({"seq_id":seq_id,"seq":seq"})
seq_data_df=pd.DataFrame(seq_data)
print(seq_data)
seq_data_df.to_csv(os.path.join(dir_path,"newadd_155098MAGs.csv"),index=False)
