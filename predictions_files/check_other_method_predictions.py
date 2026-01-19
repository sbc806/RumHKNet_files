import numpy as np
import os as os
import pandas as pd
from predictions_helpers import predictions_information

predictions_dataset_path="../../predictions/predictions_dataset/step_1/clustered"
clustered_df=pd.read_csv(os.path.join(predictions_dataset_path,"clustered_rep_seq95.csv"))
new_seqs_df=pd.read_csv(os.path.join(predictions_dataset_path,"newrun_seqs.csv"))
predictions_information(clustered_df)
predictions_information(new_seqs_df)

total_ko=pd.read_csv("../../histidine_other_methods/total_KO.txt",header=None)
total_blastp3050=pd.read_csv("../../histidine_other_methods/total_blastp3050.txt",header=None)
print(total_ko)
print(total_blastp3050)

other_methods=[total_ko,total_blast3050]
for each_method in other_methods:
  contained_1=each_method.isin(clustered_df["seq_id"])
  contained_2=each_method.isin(new_seqs_df["seq_id"])
  print(len(clustered_df),len(each_method),np.sum(contained_1))
  print(len(new_seqs_df),len(each_method),np.sum(contained_2))
