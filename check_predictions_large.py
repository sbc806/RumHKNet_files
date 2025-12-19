import numpy as np
import pandas as pd

predictions_dataset_dir_path="../predictions/predictions_dataset/step_1/clustered"
predicted_results_dir_path="../predictions/predicted_results/step_1/both/clustered"

large_df=os.path.join(predictions_dataset_dir_path,"clustered_rep_seq95_large.csv")
print("Number of sequences with length > 1500:",len(large_df))
print("Number of unique seq_id:",np.unique(large_df["seq_id"]).shape)
print("Number of unique seq:",np.unique(large_df["seq"]).shape)

large_df_length=large_df["seq"].len()
large_df_sorted=large_df[np.argsort(large_df_length)]
