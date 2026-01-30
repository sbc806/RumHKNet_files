import json
import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, reverse_dict, add_label

dataset_path="../../../predictions/predictions_results/step_4/clustered"
predictions_path="../../../predictions/predicted_results/step_4/both/clustered"

with open("../../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)


def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq=df["seq"].iloc[i]
      seq_id=df["seq_id"].iloc[i]
      pred=df.iloc[:,2].iloc[i]
      pred_other=df.iloc[:,3].iloc[i]
      f.write(f">{seq_id},{pred},{pred_other}\n")
      f.write(seq)
      if i<len(df)-1:
        f.write("\n")
















