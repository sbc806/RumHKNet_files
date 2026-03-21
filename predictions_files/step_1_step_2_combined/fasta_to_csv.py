import argparse
import os as os
import pandas as pd

from Bio import SeqIO


def convert_fasta_to_csv(dir_path,fasta_name,save_path,label):
  print(f"Converting {dir_path}/{fasta_name}.fasta")
  fasta_count=0
  
  fasta_content=SeqIO.parse(os.path.join(dir_path,f"{fasta_name}.fasta"),'fasta')
  with open(os.path.join(save_path,f"{fasta_name}.csv"),"w") as f:
    f.write("seq_id,seq\n")
    for i, fasta in enumerate(fasta_content):
      name,sequence=fasta.id,str(fasta.seq)
      # if len(sequence)<1000 or len(sequence)>5000:
        # print("Unexpected sequence length:",name, len(sequence))
      f.write(f"{name},{sequence}\n")
      fasta_count=fasta_count+1
  
  print("Number of sequences:",fasta_count)

"""
parser=argparse.ArgumentParser()
parser.add_argument("--dir_path",default=None,type=str)
parser.add_argument("--save_path",default=None,type=str)
parser.add_argument("--fasta_name",default=None,type=str)
parser.add_argument("--label",type=int)
args=parser.parse_args()
"""
# convert_fasta_to_csv(args.dir_path,args.fasta_name,args.save_path,args.label)
dir_path
convert_fasta_to_csv(
