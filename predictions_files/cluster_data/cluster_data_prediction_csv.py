from Bio import SeqIO
import os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/cluster_data"
fasta_path=os.path.join(dir_path,"newadd_155098MAGs.fasta")
"""
fasta_content=SeqIO.parse(open(fasta_path),"fasta")
seq_data=[]
for i, fasta in enumerate(fasta_content):
  seq_id,seq=fasta.id,str(fasta.seq)
  seq_data.append({"seq_id":seq_id,"seq":seq})

seq_data_df=pd.DataFrame(seq_data)
print(seq_data_df)
seq_data_df.to_csv(os.path.join(dir_path,"newadd_155098MAGs.csv"),index=False)
"""
seq_data_df=pd.read_csv(os.path.join(dir_path,"newadd_155098MAGs.csv"))

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

chunk_size=300000
# split_chunks(ko_sequences_selected,chunk_size,os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered"),"histidine_ko_no_blastp_no_rumhknet")
# split_chunks(blastp_sequences_selected,chunk_size,os.path.join(dir_path,"predictions/predictions_dataset/step_1_step_2_combined/clustered"),"histidine_blastp_ko_no_rumhknet")
