import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_14_blastp_kofamscan/cluster_data"

blastp=pd.read_csv(os.path.join(dir_path,"blastp_HK_cluster95.txt"),header=None)
kofamscan=pd.read_csv(os.path.join(dir_path,"kofam_HK_cluster95.txt"),header=None)

print("Total:",len(blastp),len(kofamscan))

print("Unique:",np.unique(blastp[0]).shape,np.unique(kofamscan[0]).shape)

print(blastp)
print(kofamscan)

isolate=pd.read_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases")
