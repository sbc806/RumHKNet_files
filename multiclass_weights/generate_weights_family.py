import numpy as np
import pandas as pd


train_multiclass = pd.read_csv("/home/schen123/projects/def-guanuofa/schen123/kinases/kinases_dataset/step_3_family_filtered/train/train.csv")
print(train_multiclass["label"].value_counts())
for i in range(0,10):
    total=len(train_multiclass)
    count=train_multiclass["label"].value_counts()[i]
    print(i,total,count)
    new_weight=None
    if np.floor(total/10/count) == 0:
        new_weight=1/5
    print(total/10/count,np.floor(total/10/count),new_weight,total/(10*count))
    print()
