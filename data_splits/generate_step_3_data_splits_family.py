import json
import numpy as np
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

def parse_histidine_kinases_fasta(fasta_path, seq_id_prefix="", ko_label_information=None, family_label_information=None):
    fasta_data = {}
    fasta_content = SeqIO.parse(open(fasta_path), 'fasta')
    for i, fasta in enumerate(fasta_content):
        name, sequence = fasta.id, str(fasta.seq)
        ko_category = name.split("_")[0]

        if ko_label_information is not None and family_label_information is not None:
            family_category = ko_label_information[ko_category]
            if family_category in family_label_information:
                label = family_label_information[family_category]
        else:
            label = None

        individual_row_information = {"seq_id": seq_id_prefix+str(i),
                                    "seq_type": "prot",
                                    "seq": sequence,
                                    "label": label}
        if label is not None:
            if family_category not in fasta_data:
                fasta_data[family_category] = [individual_row_information]
            else:
                fasta_data[family_category].append(individual_row_information)
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

histidine_kinases_file = "Final_Histidine_Kinase_668191.fasta"

histidine_kinases_labels_path = "/home/schen123/projects/def-guanuofa/schen123/kinases/kinases_dataset/Histidine_Kinases_limei.csv"

histidine_kinases_df = pd.read_csv(histidine_kinases_labels_path)
print(np.unique(histidine_kinases_df["Two-component system families"]))
print()
family_label = {}
label_file_lines = []
count = 0
for i in range(0, len(histidine_kinases_df)):
    family = histidine_kinases_df["Two-component system families"].iloc[i]
    if family != "Other families":
        if family not in family_label:
            family_label[family] = count
            label_file_lines.append(str(family_label[family]))
            count = count + 1
print(f"Number of family categories excluding Other families: {len(family_label)}")
print()

ko_category_label = {}
# label_file_lines = ["label"]
for i in range(0, len(histidine_kinases_df)):
    ko_category = histidine_kinases_df["KO number"].iloc[i]
    family = histidine_kinases_df["Two-component system families"].iloc[i]
    if ko_category not in ko_category_label:
        ko_category_label[ko_category] = family
        # label_file_lines.append(str(ko_category_label[ko_category]))
    else:
        print(f"Error. {ko_category} appears more than once.")
print(f"Number of KO categories: {len(ko_category_label)}")
print()

histidine_data = parse_histidine_kinases_fasta(os.path.join(kinases_path, histidine_kinases_file), "histidine_kinase_", ko_category_label, family_label)

all_data = histidine_data

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

train_proportion = 0.8
save_path = "/home/schen123/projects/def-guanuofa/schen123/kinases/kinases_dataset/step_3_family_filtered/protein/multi_class"
datasets = generate_dataset(all_data, train_proportion, save_path=save_path)

with open(os.path.join(save_path, "label.txt"), 'w') as f:
    for i, line in enumerate(label_file_lines):
        f.write(line + "\n")

with open(os.path.join(save_path, "family_label.json"), 'w') as f:
    json.dump(family_label, f)

with open(os.path.join(save_path, "ko_category_label.json"), 'w') as f:
    json.dump(ko_category_label, f)

train = pd.read_csv(os.path.join(save_path, "train/train.csv"))
dev = pd.read_csv(os.path.join(save_path, "dev/dev.csv"))
test = pd.read_csv(os.path.join(save_path, "test/test.csv"))

print(train)
print(dev)
print(test)
