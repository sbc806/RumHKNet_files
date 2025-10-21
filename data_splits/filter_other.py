import os
import pandas as pd

dir_path = "../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3/protein/multi_class"
save_path = "../../sbc806/RumHKNet/kinases_dataset/step_3_no_other_families/protein/multi_class"
with open(os.path.join(dir_path,"label.json"),"r") as f:
  label_information=json.load(dir_path)
family_information=pd.read_csv("../../dataset_information/133 histine kinases(Sheet1).csv")

other_families_ko=[]
for family_type in enumerate(family_information["Two-component system familes"]):
  if family_type =="Other families":
    ko_category=family_information["KO number"].iloc[i]
    other_families_ko.append(ko_category)
print("KO number for Other families:",other_families_ko")

other_families_label=[]
for ko in other_families_ko:
  other_families_label.append(label_information[ko])
splits=["train","dev,"test"]
for split in splits:
  dir=split
  csv_file=dir+".csv"
  split_dir_path=os.path.join(dir_path,dir)
  csv_path =os.path.join(split_dir_path,csv_file)

  split_df=pd.read_csv(csv_path)

  other_family_rows=split_df["label"].isin(other_families_label)
  filtered_df=split_df[~other_family_rows]

  print(f"Original shape of {split}: {split_df.shape}")
  print(f"Filtered shape of {split}: {filtered_df.shape}")
  filtered_df.to_csv(os.path.join(save_path,f"{split}/{split}.csv")
  print()
  

  
