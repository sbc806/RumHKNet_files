from Bio import SeqIO
import os
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"
fasta_path=os.path.join(dir_path,"newadd_155098MAGs.fasta"))
fasta_content=SeqIO.parse(open(dir_path),"fasta")
