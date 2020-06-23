from psequant import get_pse_data

stock = "BDO"
df = get_pse_data(stock, "2020-06-19", "2020-06-23")
print(df)


# df.to_csv("file_name.csv")


# # read the data file in as a list
# fin = open("file_name.csv", "r")
# data_list = fin.readlines()
# fin.close()
# # test it ...

# # remove list items from index 3 to 5 (inclusive)
# del data_list[0]
# # test it ...

# # write the changed data (list) to a file
# fout = open("file_name.csv", "w")
# fout.writelines(data_list)
# fout.close()
