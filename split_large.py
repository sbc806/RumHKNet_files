import pandas as pd
import os

large_path="../predictions/predictions_dataset/step_1/clustered_rep_seq95_large.csv"
large_df=pd.read_csv(large_df)
large_sequence_length=large_df["seq"].str.len()
large_df_sorted=large_df[np.argsort(large_sequence_length)]
print(large_df_sorted)
print(large_df_sorted["seq"].str.len())
large_df_sorted_subet=large_df_sorted.iloc[-1250:]
