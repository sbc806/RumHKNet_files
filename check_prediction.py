import os
import pandas as pd


predictions_path="../predictions/predicted_results/step_1/both/clustered"

def get_predictions_df(predictions_path,i):
  prediction_files=os.listdi(predictions_path)
  selected_files=[f for f in prediction_files if "small_"+str(i) in f]
  selected_files=sorted(selected_files)
  print(selected_files)
  df=None
  for f in selected_files:
    current_df=pd.read_csv(os.path.join(predictions_path,f))
