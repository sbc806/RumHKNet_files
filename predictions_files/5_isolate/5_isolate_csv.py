from Bio import SeqIO
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import fasta_to_df


dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

isolate=fasta_to_df(os.path.join(dir_path,"5_isolate.faa"))
print(isolate)
print(np.unique(isolate["seq_id"]).shape,np.unique(isolate["seq"]).shape)

small=isolate["seq"].str.len()<=1500
large=isolate["se"].str.len()>1500
print("Number of sequences <= 1500:",np.sum(small))
print("Number of sequences > 1500:",np.sum(large))

isolate[small].to_csv(os.path.join(dir_path,"predictions/predictions_datasest/step_1/clustered/5_isolate_small.csv"),index=False)
isolate[
