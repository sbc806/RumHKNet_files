import os
import numpy as np
import pandas as pd

predictions_dataset_dir_path="../predictions/predictions_dataset/step_1/clustered"
predicted_results_dir_path="../predictions/predicted_results/step_1/both/clustered"

large_df=pd.read_csv(os.path.join(predictions_dataset_dir_path,"clustered_rep_seq95_large.csv"))
print("Number of sequences with length > 1500:",len(large_df))
print("Number of unique seq_id:",np.unique(large_df["seq_id"]).shape)
print("Number of unique seq:",np.unique(large_df["seq"]).shape)

large_df_length=large_df["seq"].str.len()
large_df_sorted=large_df.iloc[np.argsort(large_df_length)]
print(len(large_df_sorted).shape)

predictions_part_1=pd.read_csv(os.path.join(predicted_results_dir_path,"large/clustered_rep_seq95_large_sorted_predicted_03_part_1.csv"))
predictions_part_2=pd.read_csv(os.path.join(predicted_results_dir_path,"large/clustered_rep_seq95_large_sorted_predicted_03_part_2.csv"))
large_sorted_predictions=pd.concat([predictions_part_1,predictions_part_2])
print("Number of predictions:",len(large_sorted_predictions))
print(np.unique(large_sorted_predictions["seq_id"].values).shape,np.unique(large_sorted_predictions["seq"].values).shape)
print("Number of shared seq_id:",np.sum(large_df_sorted["seq_id"].isin(large_sorted_predictions["seq_id"].values)))
print("Number of shared seq:",np.sum(large_df_sorted["seq"].isin(large_sorted_predictions["seq"].values)))
print("Labels:",np.unique(large_sorted_predictions["label"]))

large_sorted_predictions_kinase=large_sorted_predictions[large_sorted_predictions["label"]==1].iloc[:,0:2]
print("Number of kinases for sequences with length > 1500:",len(large_sorted_predictions_kinase))
print(large_sorted_predictions_kinase)
large_sorted_predictions_kinase.to_csv("../predictions/predictions_dataset/step_2/clustered/clustered_rep_seq95_large_sorted_kinase.csv",index=False)

def df_to_fasta(df):
  for i in range(0,len(df)):
    seq_id=df["seq_id"].iloc[i]
    seq=df["seq"].iloc[i]
    with open("../predictions/predictions_dataset/step_2/clustered/clustered_rep_seq95_large_sorted_kinase.fasta","a") as f:
      f.write(">"+seq_id+"\n")
      f.write(seq)
      if i<len(df)-1:
        f.write("\n")

df_to_fasta(large_sorted_predictions_kinase)
