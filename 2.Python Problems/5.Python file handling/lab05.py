
import pandas as pd
# open the file; set breakpoint
filename = 'c:\\Users\\admin\Desktop\Impetus\Programs\\2.Python Problems\\5.Python file handling\lab05.txt'
df1 = pd.read_table(filename)
print(df1)
print(len(df1.columns))
# data = {'Name': ['Joe', 'Mary', 'Dion', 'Kayla', 'Jose', 'Sofia', 'Erik', 'Sara'],
#         'Height(m)': [1.82, 1.60, 1.90, 1.72, 1.78, 1.63, 1.98, 1.57],
#         'Weight(kg)': [72.57, 63.50, 90.71, 66.31, 70.23, 65.12, 92.21, 65.77]}

# df1 = pd.DataFrame(data)

# data2 = {'Name': ['Average', 'Max', 'Min'],
#         'Height(m)': [df1["Height(m)"].mean(), df1["Height(m)"].max(), df1["Height(m)"].min()],
#         'Weight(kg)': [round(df1["Weight(kg)"].mean()), df1["Weight(kg)"].max(), df1["Weight(kg)"].min()]}

# df2 = pd.DataFrame((data2))
# df2 = pd.concat([df1, df2], ignore_index=True)
# df2.reset_index()

# df2_data = df2["Weight(kg)"]/df1["Height(m)"]**2
# df2_data = round(df2_data, 2)
# df2["BMI"] = df2_data
# print(df2)
# # ask
