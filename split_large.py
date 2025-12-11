import numpy as np
import pandas as pd
import os

large_path="../predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95_large.csv"
large_df=pd.read_csv(large_path)
large_sequence_length=large_df["seq"].str.len()
large_df_sorted=large_df[np.argsort(large_sequence_length)]
print(large_df_sorted)
print(large_df_sorted["seq"].str.len())
large_df_sorted_subset=large_df_sorted.iloc[-1250:]
print(large_df_sorted_subset)
print(large_df_sorted_subset.str.len())
large_df_sorted_subset.to_csv("../predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95_large_last_1250.csv",index=False)
