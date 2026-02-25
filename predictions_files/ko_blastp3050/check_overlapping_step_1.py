import pandas as pd
import os as os
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, get_interval

dataset_path="../../../predictions/predictions_dataset/step_2/clustered"
predictions_path="../../../predictions/predicted_results/step_2/both/clustered"

step_1_predicted_rbag_df=pd.read_csv("../../../RumHKNet_csv/step_1_03_step_2_03/step_1_03/step_1_clustered_newrun_rbags_predicted_03.csv")
# step_1_predicted_rbag_kinase_df=step_1_predicted_rbag_df[step_1_predicted_rbag_df.iloc[:,3]==1]
# step_2_predicted_rbag_df=pd.read_csv("../../../RumHKNet_csv/step_2_clustered_newrun_rbags_predicted_03.csv")
# step_2_predicted_rbag_histidine_df=step_2_predicted_rbag_df[step_2_predicted_rbag_df.iloc[:,3]==1]

print("total_KO")
# total_ko_df=pd.read_csv("../../../histidine_other_software/total_KO.txt",header=None)
total_ko_df=pd.read_csv("../../../histidine_other_software/total_KO_95%.txt",header=None)
print(len(total_ko_df))
print()

print("total_blastp3050")
# total_blastp3050_df=pd.read_csv("../../../histidine_other_software/total_blastp3050.txt",header=None)
total_blastp3050_df=pd.read_csv("../../../histidine_other_software/final_Blastp_HK95%_3050100.txt",header=None)
print(len(total_blastp3050_df))
print()

# predictions_information(step_1_predicted_rbag_df)

step_1_predicted_rbag_df.index=list(step_1_predicted_rbag_df["seq_id"])
print(step_1_predicted_rbag_df)
print()

print(len(total_ko_df),np.sum(total_ko_df[0].isin(step_1_predicted_rbag_df.index)))
print(len(total_blastp3050_df),np.sum(total_blastp3050_df[0].isin(step_1_predicted_rbag_df.index)))
total_ko_df["prob_step_1"]=step_1_predicted_rbag_df.loc[total_ko_df[0].values]["prob"].values
total_blastp3050_df["prob_step_1"]=step_1_predicted_rbag_df.loc[total_blastp3050_df[0].values]["prob"].values

print()

total_ko_02=total_ko_df["prob_step_1"]>=0.2
total_blastp3050_02=total_blastp3050_df["prob_step_1"]>=0.2
print(len(total_ko_df),np.sum(total_ko_02),np.sum(~total_ko_02))
print(len(total_blastp3050_df),np.sum(total_blastp3050_02),np.sum(~total_blastp3050_02))
""""
print()
print("Number of kinases predicted in step 1 using RumHKNet and threshold 0.3:",np.sum(step_1_predicted_rbag_df.iloc[:,3]==1))
print("Number of kinases predicted in step 1 using RumHKNet and threshold 0.2:",np.sum(step_1_predicted_rbag_df.iloc[:,2]>=0.2))
print("Number of kinases in common with total_KO:",np.sum(step_1_predicted_rbag_kinase_df["seq_id"].isin(total_ko_df["seq_id"].values)))
print("Number of kinases in common with total_blastp3050:",np.sum(step_1_predicted_rbag_kinase_df["seq_id"].isin(total_blastp3050_df["seq_id"].values)))
print()

print("total_KO")
intervals=[[0.0,0.1],[0.1,0.2],[0.2,0.3],[0.3,0.4],[0.4,0.5],[0.5,0.6],[0.6,0.7],[0.7,0.8],[0.8,0.9],[0.9,1.0]]
for each_interval in intervals:
  min_prob=each_interval[0]
  max_prob=each_interval[1]
  selected_rows=get_interval(total_ko_df,min_prob,max_prob,column="prob_step_1")
  print(min_prob,max_prob,len(selected_rows))

print()
print("total_blastp3050")

for each_interval in intervals:
  min_prob=each_interval[0]
  max_prob=each_interval[1]
  selected_rows=get_interval(total_blastp3050_df,min_prob,max_prob,column="prob_step_1")  
  print(min_prob,max_prob,len(selected_rows))

print(np.histogram(total_ko_df["prob_step_1"],bins=10))
print(np.histogram(total_blastp3050_df["prob_step_1"],bins=10))

print(len(total_ko_df),np.sum(total_ko_df["seq_id"].isin(step_1_predicted_rbag_df["seq_id"].values)))
print(len(total_blastp3050_df),np.sum(total_blastp3050_df["seq_id"].isin(step_1_predicted_rbag_df["seq_id"].values)))
  
step_1_predicted_rbag_kinase_02_df=step_1_predicted_rbag_df[step_1_predicted_rbag_df.iloc[:,2]>=0.2]
not_contained=~step_1_predicted_rbag_kinase_02_df["seq_id"].isin(step_1_predicted_rbag_kinase_df["seq_id"].values)
print("Number of kinases not contained:",np.sum(not_contained))
# step_1_predicted_rbag_kinase_02_df[not_contained].to_csv("../../../predictions/predictions_dataset/step_2/clustered/step_1_clustered_newrun_rbags_02_not_contained.csv",index=False)
"""








































