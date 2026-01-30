import pandas as pd
import os as os
import numpy as np

dataset_path="../../predictions/predictions_dataset/step_3/clustered"
predictions_path="../../predictions/predicted_results/step_3/both/clustered"


step_3_small_0=pd.read_csv(os.path.join(predictions_path,"step_3_11_family_dev_predicted_03.csv")).iloc[:,0:4]
step_3_small_1=pd.read_csv(os.path.join(predictions_path,"step_3_11_family_dev_predicted_03_3432_v4_0.csv")).iloc[:,0:4]

print(step_3_small_0)
print(step_3_small_1)
print(step_3_small_0.columns)
print(step_3_small_1.columns)
print()
step_3_small_1.columns=step_3_small_0.columns
print("Number of seq_id in common:",np.sum(step_3_small_0["seq_id"]==step_3_small_1["seq_id"]))
print("Number of seq in common:",np.sum(step_3_small_0["seq"]==step_3_small_1["seq"]))
print()

prob_difference=step_3_small_1.iloc[:,2]-step_3_small_0.iloc[:,2]
print(np.mean(prob_difference),np.min(prob_difference),np.max(prob_difference))
difference_argmin=np.argmin(prob_difference)
difference_argmax=np.argmax(prob_difference)
print(step_3_dev_0.iloc[difference_argmin,2],step_3_dev_1.iloc[difference_argmin,2])
print(step_3_dev_0.iloc[difference_argmax,2],step_3_dev_1.iloc[difference_argmax,2])
print()

dfs=[step_3_dev_0,step_3_dev_1]
for df in dfs:
  predictions=df.iloc[:,3]
  labels=step_3_dev["label"]
  print(predictions)
  print(labels)
  correct=np.sum(predictions==labels)
  total=len(df)
  accuracy=correct/total
  print("Accuracy:",accuracy)







