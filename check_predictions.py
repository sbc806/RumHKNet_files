import os
import pandas as pd


predictions_path="../predictions/predicted_results/step_1/both/clustered"

def get_predictions_df(predictions_path,i):
  prediction_files=os.listdir(predictions_path)
  selected_files=[f for f in prediction_files if "small_"+str(i)+"_"in f]
  selected_files=sorted(selected_files,key=lambda x:int(x.split(".csv")[0].split("_")[-1]))
  print(selected_files)
  df=None
  for f in selected_files:
    current_df=pd.read_csv(os.path.join(predictions_path,f))
    if df is None:
      df=current_df
    else:
      df=pd.concat([df,current_df])
  return df
i_df={}
for i in range(0,28):
  df_i=get_predictions_df(predictions_path,i)
  print(i)
  if df_i is not None:
    print(len(df_i))
    print(df_i)
  else:
    print("None")
  print()
dataset_path="../predictions/predictions_dataset/step_1/clustered"
for i in i_df:
  df_i=i_df[i]
  if len(df_i)<2450000:
    print(i)
    file_name=f"clustered_rep_seq95_small_{i}.csv"
    dataset=pd.read_csv(os.path.join(dataset_path,file_name))
    latest_row=len(df_i)
    print(latest_row)
    print(df_i[latest_row-1:latest_row-1+2]
    selected_df=df_i[latest_row]
    print(selected_df)
    new_file_name=f"clustered_rep_seq95_small_{i}_remaining.csv"
    selected_df.to_csv(os.path.join(dataset_path,new_file_name),index=False)
    print()
