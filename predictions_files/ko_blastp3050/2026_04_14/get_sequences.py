import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
blastp_kofamscan_path=os.path.join(dir_path,"2026_04_14_blastp_kofamscan/cluster_data")

blastp=pd.read_csv(os.path.join(blastp_kofamscan_dir_path,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(blastp_kofamscan_dir_path,"kofam_HK_cluster95.txt"),header=None)

print(len(blastp),len(kofamscan))

rumhknet_path=os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02")
rumhknet=pd.read_csv(os.path.join(rumhknet_path,"")
