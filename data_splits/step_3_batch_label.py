import json
import os
import pandas as pd
import numpy as np

dir_path="../../kinases_dataset/extra_p_133_class_v3/protein/multi_class"
with open(os.path.join(dir_path,"label.json"),"r") as f:
  ko_category_label=json.load(f)
label_ko_category={}
for ko_category in ko_category_label:
  label_ko_category[ko_category_label[ko_category]]=ko_category
with open(os.path.join("../../kinases_dataset/step_3_family_filtered/protein/multi_class/family_label.json"),"r") as f:
  family_label=json.load(f)
with open(os.path.join("../../kinases_dataset/step_3_family_filtered/protein/multi_class/ko_category_label.json"),"r") as f:
  ko_category_family=json.load(f)
train_df=pd.read_csv(os.path.join(dir_path,"train/train.csv"))
dev_df=pd.read_csv(os.path.join(dir_path,"dev/dev.csv"))
test_df=pd.read_csv(os.path.join(dir_path,"test/test.csv"))

save_path="../../kinases_dataset/step_3_11_family/protein/multi_class"
dfs=[train_df,dev_df,test_df]
names=["train/train.csv","dev/dev.csv","test/test.csv"]
for i, df in enuemrate(dfs):
  for j in range(0,len(df)):
    class_label=df["label"].iloc[j]
    ko_category=label_ko_category[str(class_label)]
    family=ko_category_family[ko_category]
    if family in family_label:
      sequence_family_label=int(family_label[family])
    else:
      sequence_family_label=10
    df.loc[j,"label"]=int(sequence_family_label)
  df.to_csv(os.path.join(save_path,names[i]),index=False)
  print(df)
  print(np.unique(df["label"]))
  print(pd.read_csv(os.path.join(save_path,names[i])))
  print()
