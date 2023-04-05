import pandas as pd

df = pd.read_csv("final_cwe_results_.csv", encoding="utf8")

df.drop_duplicates(subset=[df.columns[0]], inplace=True)

df.to_csv("final_cwe_results__.csv", index=False, encoding="utf8")
