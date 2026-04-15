import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

rumhknet_path=os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02")
rumhknet=pd.read_csv(os.path.join(rumhknet_path,"step_1_clustered_newrun_rbags_predicted_02.csv"))
print(len(rumhknet))

unique=pd.read_csv(os.path.join(dir_path,"unique_clustered_rep"))
