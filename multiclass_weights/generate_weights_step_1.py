import numpy as np
import pandas as pd
import os

dir_path="/home/schen123/scratch/kinases/kinases_dataset/extra_p_2_class_v3/protein/binary_class"
train_multiclass = pd.read_csv(os.path.join(dir_path,"train/train.csv"))
dev=pd.read_csv(os.path.join(dir_path,"dev/dev.csv"))
test=pd.read_csv(os.path.join(dir_path,"test/test.csv"))
full=pd.concat([train_multiclass,dev,test])
print(full)
print(len(full),np.sum(full["label"]==0),np.sum(full["label"]==1))
    
neg=np.sum(train_multiclass["label"]==0)
pos=np.sum(train_multiclass["label"]==1)
print("Number of counts per label:", train_multiclass["label"].value_counts())
print(neg,pos,neg/pos)
print(min(train_multiclass["label"].value_counts())/len(train_multiclass))
print(max(train_multiclass["label"].value_counts())/len(train_multiclass))
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
