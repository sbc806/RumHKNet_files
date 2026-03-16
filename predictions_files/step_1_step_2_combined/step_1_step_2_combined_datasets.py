import numpy as np
import os as os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

histidine_02=pd.read_csv(os.path.join(dir_path,"step_1_02_step_2_02/step_3_clustered_newrun_rbags_predicted_02.csv"))

ko=pd.read_csv(os.path.join(dir_path,"histidine_other_software/total_KO_95%.txt"))
total_blastp3050=pd.read_csv(os.path.join(dir_path,"histidine_other_software/final_Blastp_HK95%_3050100.txt))
