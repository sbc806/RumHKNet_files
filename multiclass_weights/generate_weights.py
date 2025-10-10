import numpy as np
import pandas as pd


train_multiclass = pd.read_csv("/home/schen123/projects/def-guanuofa/schen123/kinases/kinases_dataset/histidine_kinases_dataset_preprocessed/train/train.csv")
print(train_multiclass["label"].value_counts())
for i in range(0,133):
    total=len(train_multiclass)
    count=train_multiclass["label"].value_counts()[i]
    print(i,total,count)
    new_weight=None
    if np.floor(total/133/count) == 0:
        new_weight=1/5
    print(total/133/count,np.floor(total/133/count),new_weight)
    print()
