import os as os
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
                        "label": label}
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

histidine_data = parse_fasta(os.path.join(kinases_path, histidine_kinase_file), "histidine_kinase_", 1)
non_kinase_data = parse_fasta(os.path.join(kinases_path, non_kinase_file), "non_kinase_", 0)
other_kinase_data = parse_fasta(os.path.join(kinases_path, other_kinase_file), "other_kinase_", 1)

all_data = {"Histidine_kinase": histidine_data,
            "Non_kinase": non_kinase_data,
            "Other_kinase": other_kinase_data}

total_sequences = 0
for each_data in all_data:
    num_sequences_individual = len(all_data[each_data])
    total_sequences = total_sequences + num_sequences_individual
    minimum_individual = get_minimum_sequence_data(all_data[each_data])
    maximum_individual = get_maximum_sequence_data(all_data[each_data])
    print(each_data)
    print("Number of sequences:", num_sequences_individual)
    print("Minimum sequence_size:", len(minimum_individual["seq"]))
    print("Maximum sequence size:", len(maximum_individual["seq"]))
    print()
print("Total number of sequences:", total_sequences)
print()

histdine_sequences = [seq_data["seq"] for seq_data in histidine_data]
non_kinase_sequences = [seq_data["seq"] for seq_data in non_kinase_data]
other_kinase_sequences = [seq_data["seq"] for seq_data in other_kinase_data]

all_sequences = {"Histidine_kinase": histidine_sequences, "Non_kinase": non_kinase_sequences, "Other_kinase": other_kinase_sequences}
for sequences in all_sequences:
  print(sequences)
  print("Number of unique sequences:", np.unique(all_sequences[sequences]))
  print()

keys = list(all_sequences.keys())
for i in range(0, len(all_sequences)):
  for j in range(i+1, len(all_sequences)):
    contained = pd.Series(list(all_sequences[keys[i]])).isin(list(all_sequences[keys[j]].values()))
    print(f"Number of common sequences between {keys[0]} and {keys[i]}: {np.sum(contained)}")
    print()
