import numpy as np
import os as os
import pandas as pd

from predictions_helpers import predictions_information, fasta_to_df

# new_df=fasta_to_df("../../new/clustered95_RBAGs.fasta")
# print(new_df)
# new_df.to_csv("../../new/clustered95_RBAGs.csv",index=False)
new_df=pd.read_csv("../../new/clustered95_RBAGs.csv")
predictions_dataset_path="../../predictions/predictions_dataset/step_1/clustered"
clustered_df=pd.read_csv(os.path.join(predictions_dataset_path,"clustered_rep_seq95.csv"))
newrun_seqs_df=pd.read_csv(os.path.join(predictions_dataset_path,"newrun_seqs.csv"))
# predictions_information(clustered_df)
# predictions_information(new_seqs_df)
# new_df=fasta_to_df("../../new/clustered95_RBAGs.fasta")
# print(new_df)
# new_df.to_csv("../../new/clustered95_RBAFs.fasta")
print("Number of sequences in common between clustered_rep_seq95 and newrun_seqs:",np.sum(clustered_df["seq_id"].isin(newrun_seqs_df["seq_id"].values)))
print("Number of sequences in common between clustered_rep_seq95 and new:", np.sum(clustered_df["seq_id"].isin(new_df["seq_id"].values)))
print("Number of sequences in common between newrun_seqs and new:",np.sum(newrun_seqs_df["seq_id"].isin(new_df["seq_id"].values)))

contained_1=new_df["seq_id"].isin(clustered_rep_seq95_df["seq_id"].values)
contained_2=new_df["seq_id"].isin(newrun_seqs_df["seq_id"].values)
extra=~contained_1&~contained_2
print(np.sum(contained_1),np.sum(contained_2),np.sum(extra))
new_df[extra].to_csv("../../new/clustered95_RBAGs_extra.csv",index=False)
total_ko=pd.read_csv("../../histidine_other_software/total_KO.txt",header=None)
total_blastp3050=pd.read_csv("../../histidine_other_software/total_blastp3050.txt",header=None)

# Sequences in new and total_KO
# sSequences in new and totalKoO and clustered_rep_seq95
# Sequences in new and total KO and not in clustered_rep_seq95

# Sequences in new and blastp3050
# Seuqneces in new and totalKO and clustered_rep_seq95
# Sequences in new and total blastp3050 and not in newrun_seqs

# Seuqneces not in clustered_rep_seq95, newrun_seqs, exclusive totalKO, and total blastp3050











