import numpy as np
import pandas as pd


train_multiclass = pd.read_csv("/home/schen123/scratch/kinases/kinases_dataset/extra_p_2_class_v3_kinases_only/protein/binary_class/train/train.csv")
print("Number of counts per label:", train_multiclass["label"].value_counts())
print(min(train_multiclass["label"].value_counts())/max(train_multiclass["label"].value_counts()))
print(min(train_multiclass["label"].value_counts())/ln(train_multiclass))
print(max(train_multiclasss["label"].value_counts())/len(train_multiclass))
"""
for i in range(0,133):
    total=len(train_multiclass)
    count=train_multiclass["label"].value_counts()[i]
    print(i,total,count)
    new_weight=None
    if np.floor(total/133/count) == 0:
        new_weight=1/5
    print(total/133/0.2/count,np.floor(total/133/0.2/count),total/133/count,np.floor(total/133/count),new_weight,total/(count*133))
    print()
  """
