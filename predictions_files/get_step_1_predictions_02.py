import os as os

import pandas as pd

step_1_predictions_03_df=pd.read_csv("../../RumHKNet_csv/step_1_03_step_2_03/step_1_03/step_1_clustered_newrun_rbags_predicted_03.csv")
print(step_1_predictions_03_df)
step_1_predictions_03_df=step_1_predictions_03_df.iloc[:,0:3]
step_1_predictions_03_df["pred"]=step_1_predictions_03_df["prob"]>=0.2
print(np.sum(step_1_predictions_03_df["pred"]))

step_1_predictions_03_df.to_csv("../../RumHKNet_csv/step_1_02_step_2_02/step_1_clustered_newrun_rbags_predicted_02.csv",index=False)



