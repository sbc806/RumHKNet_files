import json
import os as os
import pandas as pd
import numpy as np
from predictions_helpers import predictions_information, reverse_dict, add_label


# Want to piar family to KO
# TGet full dataset of histidne kinases used for training, train, dev, and test
# Connect number label to ko category

# Subetp, connect ko category to afmily

# After, ogo through family labels
# Match seq_id, get numerical batcko label then actual ko label then get family label

other_label={}
ko_train_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/train/train.csv")
ko_dev_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/dev/dev.csv")
ko_test_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/test/test.csv")
histidine_full_df=pd.concat([ko_train_df,ko_dev_df,ko_test_df])
print("Number of histidine kinases:",len(histidine_full_df))

step_3_train_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/step_3_11_family/protein/multi_class/train/train.csv")
step_3_dev_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/step_3_11_family/protein/multi_class/dev/dev.csv")
step_3_test_df=pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/step_3_11_family/protein/multi_class/test/test.csv")
step_3_full_df=pd.concat([step_3_train_df,step_3_dev_df,step_3_test_df])
print("Number of histidine kinases for step 3:",len(step_3_full_df))
print(step_3_full_df.columns)
histidine_information_df=pd.read_csv("../../Histidine_Kinases_limei.csv")
print(histidine_information_df.columns)

ko_family={}
for i in range(0,len(histidine_information_df)):
  ko=histidine_information_df.iloc[i,0]
  family=histidine_information_df.iloc[i,5]
  if isinstance(family,float):
    print(ko+" has nan for family")
    family="Other families"
  ko_family[ko]=family
print("Contained:",np.sum(step_3_full_df["seq_id"].isin(histidine_full_df["seq_id"].values)))
print()

print("ko_family:",ko_family,len(ko_family))
print("Number of families:",np.unique(np.array(list(ko_family.values()))).shape)
with open("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)
print("ko_label:",ko_label)
label_ko=reverse_dict(ko_label)
for each_family in np.unique(step_3_full_df["label"]):
  step_3_selected_df=step_3_full_df[step_3_full_df["label"]==each_family]
  seq_id=step_3_selected_df.iloc[0]["seq_id"]
  location=np.where(histidine_full_df["seq_id"]==seq_id)[0]
  print(each_family,seq_id,location)
  assert len(location)==1
  ko_number=histidine_full_df["label"].iloc[location[0]]
  ko=label_ko[str(ko_number)]
  family=ko_family[ko]
  print(ko_number,ko,family)
  other_label[family]=int(each_family)
  print()
print(other_label)

with open("../../sbc806/RumHKNet/kinases_dataset/step_3_11_family/protein/multi_class/label.json","w") as f:
  json.dump(other_label,f)


small_histidine_df_new=add_label(small_histidine_df,reverse_dict(other_label))
print(small_histidine_df_new)
large_histidine_df_new=add_label(large_histidine_df,reverse_dict(other_label))
print(large_histidine_df_new)

print("batch:",np.unique(pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/train/train.csv")["batch"]))
print("batch:",np.unique(pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/dev/dev.csv")["batch"]))
print("batch:",np.unique(pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/test/test.csv")["batch"]))


























































