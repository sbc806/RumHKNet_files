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
with open(os.path.join("../../kinases_dataset/step_3_family_filtered/protein/multi_class/family_label.json","r") as f:
  family_label=json.load(f)
with open(os.path.join("../../kinases_dataset/step_3_family_filtered/protein/multi_class/ko_category_label.json"),"r") as f:
  ko_category_family=json.load(f)
train_df=pd.read_csv(os.path.join(dir_path,"train/train.csv"))
dev_df=pd.read_csv(os.path.join(dir_path,"dev/dev.csv"))
test_df=pd.read_csv(os.path.join(dir_path,"test/test.csv"))

dfs=[train_df,dev_df,test_df]
for df in dfs:
  for i in range(0,len(df)):
    class_label=df["label"].iloc[i]
    ko_category=label_ko_category[str(class_label)]
    if ko_category in ko_category_family:
      family_label=ko_category_family[ko_category]
    else:
      family_label=10
    df.loc[i,"label"]=int(family_label)
  print(df)
  print(np.unique(df["label"]))
  print()
