import os
impotr numpy as np
import pandas aspd

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"5_isolate_step_2_histidine_kinase_small_predicted_02_v2.csv"))
print(len(small))

print(small)
print(small.columns)

small_selected=small[["seq_id","seq","top1_label"]]
small_selected.iloc[np.where(small_selected["batch"]==-10)[0],2]=-1
