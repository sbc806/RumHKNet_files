import os
import numpy as np
import pandas as pd

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

large=pd.read_csv(os.path.join(dataset_path,"2026_04_22_clustered95_rep_seq_large.csv"))
print(large)
lengths_argsort=np.argsort(large["seq"].str.len())
print(lengths_argsort)
large_argsort=lengths_argsort.iloc[lengths_argsort.values]
print(large_argsort["seq"].str.len())
less_equal_10000=large_argsort.str.len()<=10000

large_argsort_1=large_argsort[less_equal_10000]
large_argsort_2=large_argsort[~less_equal_10000]
