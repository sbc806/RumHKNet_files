import os as os
import pandas as pd
import numpy as np

step_1_predicted_df=pd.read_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03_old.csv")
step_1_predicted_df.iloc[:,1:].to_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03.csv")
"""
clustered95_rbags=pd.read_csv("../../../new/clustered95_RBAGs.csv")
print(step_1_predicted_df)
print(clustered95_rbags)
seq_id_argsort_1=np.argsort(step_1_predicted_df["seq_id"].values)
step_1_predicted_df=step_1_predicted_df.iloc[seq_id_argsort_1]
seq_id_argsort_2=np.argsort(clustered95_rbags["seq_id"].values)
clustered95_rbags=clustered95_rbags.iloc[seq_id_argsort_2]
print(len(step_1_predicted_df),len(clustered95_rbags))
print(np.sum(step_1_predicted_df["seq_id"].values==clustered95_rbags["seq_id"].values))
print(np.sum(step_1_predicted_df["seq"].values==clustered95_rbags["seq"].values))
"""

