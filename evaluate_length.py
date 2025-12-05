import os as os
import numpy as np
import pandas as pd
from Bio import SeqIO
import random


def parse_fasta(fasta_path, seq_id_prefix="", label=None):
    fasta_data = []
    fasta_content = SeqIO.parse(open(fasta_path), 'fasta')
    for i, fasta in enumerate(fasta_content):
        name, sequence = fasta.id, str(fasta.seq)
        fasta_individual = {"seq_id": seq_id_prefix+str(i),
                        "seq_type": "prot",
                        "seq": sequence,
                        "seq_length": len(sequence)}
        fasta_data.append(fasta_individual)
    return fasta_data


def filter_sequence_size(fasta_data, min_length, max_length):
    fasta_data_filtered = []
    for each_data in fasta_data:
        sequence = each_data["seq"]
        if len(sequence) >= min_length and len(sequence) <= max_length:
            fasta_data_filtered.append(each_data)
    return fasta_data_filtered


def get_minimum_sequence_data(fasta_data):
    fasta_individual_minimum = fasta_data[0]
    minimum_sequence_size = len(fasta_individual_minimum["seq"])
    for i in range(1, len(fasta_data)):
        fasta_individual_current = fasta_data[i]
        current_sequence_size = len(fasta_individual_current["seq"])
        if current_sequence_size < minimum_sequence_size:
            fasta_individual_minimum = fasta_individual_current
            minimum_sequence_size = current_sequence_size
    return fasta_individual_minimum


def get_maximum_sequence_data(fasta_data):
    fasta_individual_maximum = fasta_data[0]
    maximum_sequence_size = len(fasta_individual_maximum["seq"])
    for i in range(1, len(fasta_data)):
        fasta_individual_current = fasta_data[i]
        current_sequence_size = len(fasta_individual_current["seq"])
        if current_sequence_size > maximum_sequence_size:
            fasta_individual_maximum = fasta_individual_current
            maximum_sequence_size = current_sequence_size
    return fasta_individual_maximum


def generate_dataset(all_data, train_proportion, save_path=""):
    header = ["seq_id", "seq_type","seq", "label"]
    datasets = [[], [], []]
    for each_data in all_data:
        current_data = all_data[each_data]
        data_num_samples = len(current_data)
        train_num_samples = int(data_num_samples * train_proportion)
        dev_proportion = ((1-train_proportion) / 2)
        dev_num_samples = int(dev_proportion * data_num_samples) + 1

        datasets[0].extend(current_data[0: train_num_samples])
        datasets[1].extend(current_data[train_num_samples: train_num_samples + dev_num_samples])
        datasets[2].extend(current_data[train_num_samples + dev_num_samples:])

        print(each_data)
        print("train_num_samples:", train_num_samples)
        print("dev_num_samples:", dev_num_samples)
        print("Number of train samples:", train_num_samples-0)
        print("Number of dev samples:", (train_num_samples+dev_num_samples)-train_num_samples)
        print("Number of test samples:", data_num_samples-(train_num_samples+dev_num_samples))
        print()

    for _ in range(10):
        random.shuffle(datasets[0])

    pd.DataFrame(datasets[0], columns=header).to_csv(os.path.join(save_path, "train/train.csv"), index=False)
    pd.DataFrame(datasets[1], columns=header).to_csv(os.path.join(save_path, "dev/dev.csv"), index=False)
    pd.DataFrame(datasets[2], columns=header).to_csv(os.path.join(save_path, "test/test.csv"), index=False)
    return datasets


kinases_path = "/home/schen123/projects/def-guanuofa/schen123/kinases/kinases_dataset/kinases_dataset_unzipped"

histidine_kinase_file = "Final_Histidine_Kinase_668191.fasta"
non_kinase_file = "Non_Kinase_527009.fasta"
other_kinase_file = "Final_other_kinase_760926.fasta"

histidine_data = parse_fasta("/home/schen123/scratch/clustered_rep_seq95.fasta", "seq_", None)

# all_data = {"Histidine_kinase": sequence_data}
# sequence_df=pd.DataFrame(histidine_data)
# sequence_df=pd.read_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/train_0_100000.csv")
sequence_df["seq_length"]=sequence_df["seq"].str.len()
total_sequences=len(sequence_df)
print("Total number of sequences:", total_sequences)
print("Minimum sequence length:", np.min(sequence_df["seq_length"]))
print("Maximum sequence length:", np.max(sequence_df["seq_length"]))
print("Average sequence length:", np.mean(sequence_df["seq_length"]))
print()

ranges=[(3432,10000),(10000,20000),(20000,30000),(30000,40000)]
for each_range in ranges:
    start=each_range[0]
    end=each_range[1]
    contained=(sequence_df["seq_length"]>start)&(sequence_df["seq_length"]<=end)
    print(f"{np.sum(contained)} sequences with length in {each_range}")
print("Number of sequences >=1500:",np.sum(sequence_df["seq_length"]>=1500))
print("Number of sequences <1500:",np.sum(sequence_df["seq_length"]<1500))
print("Number of sequences >1500:",np.sum(sequence_df["seq_length"]>1500))
print("Number of sequences <=1500:",np.sum(sequence_df["seq_length"]<=1500))

sequence_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/clustered_rep_seq95.csv",index=False)
