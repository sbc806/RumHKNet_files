import os
import pandas as pd


predictions_path="../predictions/predicted_results/step_1/both/clustered"

def get_predictions_df(predictions_path,i):
  prediction_files=os.listdir(predictions_path)
  selected_files=[f for f in prediction_files if "small_"+str(i) in f]
  selected_files=sorted(selected_files)
  print(selected_files)
  df=None
  for f in selected_files:
    current_df=pd.read_csv(os.path.join(predictions_path,f))
    if df is None:
      df=current_df
    else:
      df=pd.concat([df,current_df])
  return df

for i in range(0,28):
  df_i=get_predictions_df(predictions_path,i)
  print(i)
  if df_i is not None:
    print(len(df_i))
    print(df_i)
  else:
    print("None")
  print()
