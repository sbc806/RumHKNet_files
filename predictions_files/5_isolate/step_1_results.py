import os
import pandas as pd
import numpy as np

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clstered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_v2=pd.read_csv(os.path.join(predictions_path,"5_isolate_small_predicted_02_v2.csv"))
small_v3=pd.read_csv(os.path.join(predictions_path,"5_isolate_small_predicted_02_1500_v3_0.csv"))

print(len(small_v2),len(small_v3))
print(np.mean(small_v3["prob"]-small_v2["prob"]))
print(np.mean(round(small_v3["prob"],5)-round(small_v2["prob"],5)))
print(np.sum(small_v2["label"].values==small_v3["pred"].values),np.sum(small_v2["label"].values!=small_v3["pred"].values))

small_v2[small_v2["label"]==1][["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/5_isolate_step_1_kinase_small.csv",index=False)

print(np.sum(small_v2["prob"]>=0.2),np.sum(small_v2["label"]==1))
print(np.sum(small_v3["prob"]>=0.2),np.sum(small_v3["pred"]==1))

large=pd.read_csv(os.path.join(predictions_path,"5_isolate_large_predicted_02_v2.csv"))
print(len(large))
print(np.sum(large["prob"]>=0.2),np.sum(large["label"]==1))
