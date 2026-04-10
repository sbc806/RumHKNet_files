from Bio import SeqIO
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import fasta_to_df


dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

isolate=fasta_to_df
