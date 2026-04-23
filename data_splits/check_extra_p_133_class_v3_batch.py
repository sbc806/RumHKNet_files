import os
import numpy as np
import pandas as pd

dataset_path="../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class"

train_path=os.path.join(dataset_path,"train/train.csv")
dev_path=os.path.join(dataset_path,"dev/dev.csv")
test_path=os.path.join(dataset_path,"test/test.csv")

train=pd.read_csv(train_path)
dev=pd.read_csv(dev_path)
test=pd.read_csv(test_path)

print(train)
print(dev)
print(test)
print(len(train)+len(dev)+len(test))

dfs={"train":train,"dev":dev,"test":test}
for df in dfs:
  print(df)
  chosen_df=dfs[df]
  print("Unique labels:",np.unique(chosen_df["label"]))
  labels=np.unique(chosen_df["label"])
  for label in labels:
    print(f"Count for {label}:",np.sum(chosen_df["label"]==label))
  print()
