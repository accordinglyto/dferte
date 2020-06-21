from psequant import get_pse_data

df = get_pse_data("GTCAP", "2020-01-3", "2020-06-19")
df.to_csv("file_name.csv")


# read the data file in as a list
fin = open("file_name.csv", "r")
data_list = fin.readlines()
fin.close()
# test it ...

# remove list items from index 3 to 5 (inclusive)
del data_list[0]
# test it ...

# write the changed data (list) to a file
fout = open("file_name.csv", "w")
fout.writelines(data_list)
fout.close()
