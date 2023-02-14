# ========================== pandas Module ==========================

import pandas as pd

df = pd.read_csv(r"data\survey_results_public.csv")

# print(df)

# print(df.shape) # attribue

# print(df.info())

pd.set_option('display.max_columns', 79)

print(df)

