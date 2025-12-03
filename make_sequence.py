import os
import pandas as pd
import random
import string

save_path="../predictions/predictions_dataset/step_1"

num_sequences=15
desired_length=34551
seq_id=[]
seq=[]
for i in range(0,num_sequences):
  sequence=''.join(random.choices(string.ascii_uppercase,k=desired_length))
  seq_id.append("fake_seq_"+str(i))
  seq.append(sequence)
df=pd.DataFrame({"seq_id":seq_id,"seq":seq})
print(df)
df.to_csv(os.path.join(save_path,"sequences_34551.csv"),index=False)
