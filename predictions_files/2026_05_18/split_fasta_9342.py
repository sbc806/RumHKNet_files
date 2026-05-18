from Bio import SeqIO
import numpy as np
import os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_cluster_data"
fasta_path=os.path.join(dir_path,"9342_all_proteins_newrun.faa")
dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

fasta_content=SeqIO.parse(open(fasta_path),"fasta")
seq_data=[]
for i, fasta in enumerate(fasta_content):
  seq_id,seq=fasta.id,str(fasta.seq)
  seq_data.append({"seq_id":seq_id,"seq":seq})

seq_data_df=pd.DataFrame(seq_data)
print(seq_data_df)
# seq_data_df.to_csv(os.path.join(dir_path,"newadd_155098MAGs.csv"),index=False)

# seq_data_df=pd.read_csv(os.path.join(dir_path,"newadd_155098MAGs.csv"))

def split_chunks(df,chunk_size,save_path,save_name):
  small=df["seq"].str.len()<=1500
  large=df["seq"].str.len()>1500
  print(np.sum(small),np.sum(large))
        
  df_small=df[small]
  df_large=df[large]
  num_splits=len(df)//chunk_size+1
  for i in range(num_splits):
    start=i*chunk_size
    end=start+chunk_size
    print("Start:",start,"End:",end)
    df_small_i=df_small[start:end]
    df_small_i.to_csv(os.path.join(save_path,f"{save_name}_small_{i}.csv"),index=False)
  df_large.to_csv(os.path.join(save_path,f"{save_name}_large.csv"),index=False)
  print(max(df_small["seq"].str.len()),max(df_large["seq"].str.len()))
  
chunk_size=1200000
# split_chunks(seq_data_df,chunk_size,dataset_path,"2026_04_22_clustered95_rep_seq")
