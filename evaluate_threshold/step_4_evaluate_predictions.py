import pandas as pd
import os as os
import numpy as np

dataset_path="../../predictions/predictions_dataset/step_3/"
predictions_path="../../predictions/predicted_results/step_3/both"


step_4_dev=pd.read_csv("../../kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/dev/dev.csv")
step_4_dev_0=pd.read_csv(os.path.join(predictions_path,"extra_p_133_class_v3_batch_dev_predicted_03.csv"))
# step_4_dev_1=pd.read_csv(os.path.join(predictions_path,"extra_p_133_class_v3_batch_dev_predicted_03_3432_v4_0.csv"))

print(step_4_dev_0)
# print(step_4_dev_1)
print(step_4_dev_0.columns)
# print(step_4_dev_1.columns)
print()
"""
print("Number of seq_id in common:",np.sum(step_4_dev_0["seq_id"]==step_4_dev_1["seq_id"]))
print("Number of seq in common:",np.sum(step_4_dev_0["seq"]==step_4_dev_1["seq"]))
print()

prob_difference=step_4_dev_1.iloc[:,2]-step_4_dev_0.iloc[:,2]
print(np.mean(prob_difference),np.min(prob_difference),np.max(prob_difference))
difference_argmin=np.argmin(prob_difference)
difference_argmax=np.argmax(prob_difference)
print(step_4_dev_0.iloc[difference_argmin,2],step_4_dev_1.iloc[difference_argmin,2])
print(step_4_dev_0.iloc[difference_argmax,2],step_4_dev_1.iloc[difference_argmax,2])
print()
"""
dfs=[step_4_dev_0]
for df in dfs:
  predictions=df.iloc[:,3]
  labels=step_3_dev["label"]
  print(predictions)
  print(labels)
  correct=np.sum(predictions==labels)
  total=len(df)
  accuracy=correct/total
  print("Accuracy:",accuracy)









