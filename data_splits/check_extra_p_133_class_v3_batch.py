import os
import numpyas np
import pandas as pd

dataset_path="../../kinases/step_3_11_family/protein/multi_class"

train_path=os.path.join(dataset_path,"train/train.csv")
dev_path=os.path.join(dataset_path,"dev/dev.csv")
test_path=os.path.join(dataset_path,"test/test.csv")

train=pd.read_csv(train_path)
dev=pd.read_csv(dev_path)
test=pd.read_csv(test_path)
