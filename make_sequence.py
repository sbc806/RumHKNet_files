import os
import pandas as pd
import random
import string

save_path="../predictions/predictions_dataset/step_1"

num_sequences=1000
desired_length=1500
seq_id=[]
seq=[]
for i in range(0,num_sequences):
  # sequence=''.join(random.choices(string.ascii_uppercase,k=desired_length))
  sequence="M"*desired_length
  seq_id.append("fake_seq_"+str(i))
  seq.append(sequence)
df_v2=pd.DataFrame({"seq_id":seq_id,"seq_type":["prot" for i in range(0,num_sequences)],"seq":seq})
print(df_v2)
df_v2[0:3].to_csv(os.path.join(save_path,f"sequences_{desired_length}_v2.csv"),index=False)
df_v3=pd.DataFrame({"seq_id":seq_id,"seq":seq})
print(df_v3)
df_v3.to_csv(os.path.join(save_path,f"sequences_{desired_length}_v3.csv"),index=False)
