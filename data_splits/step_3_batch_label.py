import os
import pandas as pd
import numpy as np

dir_path="../../kinases_dataset/extra_p_133_class_v3"
with open(os.path.join(dir_path,"label.jsn","r")) as f:
  ko_category_label=json.load(f)
label_ko_category={}
for ko_category in ko_category_label:
  label_ko_category[ko_category_label[ko_category]]=ko_category
train_df=pd.read_csv(os.path.join(dir_path,"train/train.csv"))
dev_df=pd.read_csv(os.pat.join(dir_path,"dev/dev.csv"))
test_df=pd.read_csv(os.path.join(dir_path,"test/test.csv"))

dfs=[train_df,dev_df,test_df]
for df in dfs:
  for i in range(0,len(df)):
    class_label=df["label"].iloc[i]
    ko_category=label_ko_category[class_label]
    if ko_category in ko_category_family:
      family_label=ko_category_family[ko_category]
    else:
      family_label="10"
    df["label"].iloc[i]=family_label
