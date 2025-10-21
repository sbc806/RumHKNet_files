import json
import os
import pandas as pd

dir_path = "../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3/protein/multi_class"
save_path = "../../sbc806/RumHKNet/kinases_dataset/step_3_no_other_families/protein/multi_class"
# with open(os.path.join(dir_path,"label.json"),"r") as f:
  # print(dir_path)
  # label_information=json.loads(dir_path)

label_information={"K07679": "0", "K13587": "1", "K11527": "2", "K07636": "3", "K07652": "4", "K02482": "5", "K11354": "6", "K02484": "7", "K03407": "8", "K07678": "9", "K07709": "10", "K07651": "11", "K20974": "12", "K14986": "13", "K02480": "14", "K07638": "15", "K07778": "16", "K19694": "17", "K07644": "18", "K00936": "19", "K07646": "20", "K07675": "21", "K13598": "22", "K07654": "23", "K07642": "24", "K11383": "25", "K07645": "26", "K07708": "27", "K07637": "28", "K07710": "29", "K10125": "30", "K11357": "31", "K18940": "32", "K07649": "33", "K07716": "34", "K02491": "35", "K18350": "36", "K18351": "37", "K02476": "38", "K14982": "39", "K07640": "40", "K07768": "41", "K02668": "42", "K06596": "43", "K14980": "44", "K20975": "45", "K07656": "46", "K07653": "47", "K07777": "48", "K07718": "49", "K19691": "50", "K07648": "51", "K20971": "52", "K07639": "53", "K15011": "54", "K18345": "55", "K07673": "56", "K11356": "57", "K11617": "58", "K19690": "59", "K19081": "60", "K13533": "61", "K07711": "62", "K07677": "63", "K07704": "64", "K07641": "65", "K19616": "66", "K13490": "67", "K07697": "68", "K11711": "69", "K07683": "70", "K10942": "71", "K20487": "72", "K14489": "73", "K02478": "74", "K19692": "75", "K13532": "76", "K11526": "77", "K11633": "78", "K20973": "79", "K11231": "80", "K07698": "81", "K10715": "82", "K11520": "83", "K07655": "84", "K11614": "85", "K07650": "86", "K18072": "87", "K07647": "88", "K10819": "89", "K07643": "90", "K13040": "91", "K07717": "92", "K20972": "93", "K07769": "94", "K17060": "95", "K19609": "96", "K11637": "97", "K19661": "98", "K07674": "99", "K27882": "100", "K18143": "101", "K11629": "102", "K07700": "103", "K07681": "104", "K11328": "105", "K08479": "106", "K27076": "107", "K10916": "108", "K11623": "109", "K08475": "110", "K11691": "111", "K20263": "112", "K07682": "113", "K07680": "114", "K19621": "115", "K10681": "116", "K27884": "117", "K10909": "118", "K07701": "119", "K18986": "120", "K08082": "121", "K14978": "122", "K15850": "123", "K02486": "124", "K19077": "125", "K27105": "126", "K07706": "127", "K25212": "128", "K02489": "129", "K14988": "130", "K11640": "131", "K12294": "132"}
family_information=pd.read_csv("../../dataset_information/133 histine kinases(Sheet1) (1).csv")

other_families_ko=[]
for family_type in enumerate(family_information["Two-component system familes"]):
  if family_type =="Other families":
    ko_category=family_information["KO number"].iloc[i]
    other_families_ko.append(ko_category)
print("KO number for Other families:",other_families_ko)

other_families_label=[]
for ko in other_families_ko:
  other_families_label.append(label_information[ko])
splits=["train","dev","test"]
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
  filtered_df.to_csv(os.path.join(save_path,f"{split}/{split}.csv"))
  print()
  

  
