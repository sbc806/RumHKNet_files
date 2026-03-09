import os as os
import numpy as np
import pandas as pd

dir_path="../sbc806/RumHKNet_develop/kinases_dataaset/step_1_non_kinases_preprocessed/protein/binary_class"
train_path=os.path.join(dir_path,"train/train.csv")
dev_path=os.path.join(dir_path,"dev/dev.csv")
test_path=os.path.join(dir_path,"test/test.csv")

train_df=pd.read_csv(train_path)
dev_df=pd.read_csv(dev_path)
test_df=pd.read_csv(test_path)

all_df=pd.concat([train_df,dev_df,test_df])

print("Number for train:",len(train_df))
print("Number for dev:",len(dev_df))
print("Number for test:",len(test_df))
print("80% is:",0.80*len(all_df))
print("10% is:",0.10*len(all_df))

dfs=[train_df,dev_df,test_df,all_df]
prots=["histidine_kinase_","non_kinase_","other_kinase_"]
for df in dfs:
  for prot in prots:
    print(np.sum(df["seq_id"].str.contains(prot)))

