from psequant import get_pse_data

df = get_pse_data("BDO", "2020-05-28", "2020-06-20")
df.to_csv("file_name.csv")

