import pandas

count = 0
with pd.read_csv("../predictions/predictions_dataset/step_1/clustered/clustered_rep_seq95_small_0.csv,chunksize=50) as csv_reader:
  for chunk in csv_reader:
    count=count+1
print(count)
