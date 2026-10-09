# series

# import pandas as pd
# a=pd.Series([10,20,30],index=["x","y","z"])
# print(a)

# import pandas as pd
# a=pd.Series([10,20,30])
# print(a)

# indexing

# import pandas as pd
# a=pd.Series([10,20,30])
# print(a[1])

# import pandas as pd
# a=pd.Series([10,20,30],index=["x","y","z"])
# print(a["y"])


# slicing

# import pandas as pd
# a=pd.Series([10,20,30,40])
# print(a[1:3])


# calculation

# import pandas as pd
# a=pd.Series([10,20,30,40])
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.mean())

# filtering

# import pandas as pd
# a=pd.Series([10,20,30,40])
# print(a[a>20])

# find missing value

# import pandas as pd
# a=pd.Series([10,None,30,40])
# print(a.isnull())

# import pandas as pd
# a=pd.Series([10,None,30,None,50])
# print(a.isnull())
# print(a.dropna())
# print(a.fillna(0))


# import pandas as pd
# a=pd.Series({
#     "math" : 85,
#     "python" : 92,
#     "ml" : 78,
#     "pandas" : 88
# })
# print(a)
# print(a["python"])


# import pandas as pd
# a=pd.Series([10,20,30,40,50])
# print(a.dtype)
# print(a.values)
# print(a.index)


# import pandas as pd
# a=pd.Series({
#     "math" : 85,
#     "python" : 92,
#     "ml" : 78,
#     "pandas" : 88,
#     "sql" : 95
# })    
# print(a[a>80])


# import pandas as pd
# a=pd.Series([10,None,30,None,50])
# print(a.notnull())


# data frame creation

# import pandas as pd
# data={
#     "Name": ["Pushkar","Rahul","Aman"],
#     "Marks": [85, 72, 91]
# }
# df = pd.DataFrame(data)
# print(df)

# single column selection

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# print(data)
# print(data["name"])

# multiple column selection 

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# # print(data)
# print(data[["name","age"]])

# indexing

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# print(data)
# print(data["name"][0])

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# # print(data)
# print(data["name"][2])


# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# # print(data)
# print(data["age"][1])

# slicing

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# # print(data)
# print(data["name"][0:2])

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45]
# })
# # print(data)
# print(data["age"][1:3])

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# # print(data)
# print(data)

# column modified/updated

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# data["age"] = [18,20,25]
# print(data)

# row selection with loc

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.loc[1])


# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.loc[0:2])


# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.loc[0:1,["name","age"]])


# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.loc[:,["name","city"]])

# row selection with iloc

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.iloc[0:2])

# import pandas as pd
# data=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar"],
#     "age" : [15,12,45],
#     "city" : ["chandigarh","delhi","mumbai"]
# })
# print(data.iloc[0:2,0:2])


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.sort_values("marks",ascending=False))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.sort_values("marks",ascending=True))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.head())  

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.tail())


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.head(2))

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.tail(2))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.head())  

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.tail())


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.head(2))

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.shape)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman","sharma"],
#     "marks": [85, 72, 91,215]
# })
# print(a.index)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.columns)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91]
# })
# print(a.dtypes)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# print(a.dtypes)

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# a.loc[3] = ["rohit", 78, 20]
# print(a)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# a.loc[3] = ["rohit", 78, 20]
# print(a)

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# print(a.drop(1))


# column delete

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# print(a.drop("age",axis=1))


# rename column


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# print(a.rename(columns={"marks" : "score"}))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "aman"],
#     "marks": [85, 72, 91],
#     "age" : [18,20,19]
# })
# print(a.rename(columns={"age" : "years"}))


# find duplicate

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, 72, 85]
# })
# print(a.duplicated())



# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, 72, 85]
# })
# print(a.drop_duplicates())


# finding missing value


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, None, 85]
# })
# print(a.isnull()) 


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, None, 85]
# })
# print(a.notnull())


# filtering

# import pandas as pd
# a=pd.DataFrame({
#     "name" : ["pushkar","rahul","aman"],
#     "age" : [18,20,19],
#     "marks" : [85,72,91]
# })
# a["age"] = [19,21,20]
# print(a[a["marks"]>80]["marks"])

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, None, 85]
# })
# print(a.dropna()) 

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, None, 85]
# })
# print(a.fillna(0)) 

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, 25, 85]
# })
# print(a["marks"].astype(float))


# value_count

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["pushkar", "rahul", "pushkar"],
#     "marks": [85, 25, 85]
# })
# print(a["name"].value_counts())



# import pandas as pd
# a=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar","chirag"],
#     "age" : [15,12,18,14],
#     "marks" : [90,95,91,76],
#     "roll" : [102,130,105,108]
# })
# print(a["name"].unique())


# import pandas as pd
# a=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar","chirag"],
#     "age" : [15,12,18,14],
#     "marks" : [90,95,91,76],
#     "roll" : [102,130,105,108]
# })
# print(a["name"].nunique())


# import pandas as pd
# a=pd.DataFrame({
#     "name" : ["pushkar","sharma","kumar","chirag"],
#     "age" : [15,12,18,14],
#     "marks" : [90,95,91,76],
#     "roll" : [102,130,105,108]
# })
# print(a["marks"].describe())


# groupby

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.groupby("city")["marks"].sum()["Delhi"])


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.groupby("city")["marks"].mean())


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.groupby("city")["name"].count())


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.groupby("city")["marks"].max())



# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.groupby("city")["marks"].aggregate(["mean","max","min"]))


# set index

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.set_index("city"))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.set_index("name"))


# reset index


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.reset_index(drop=False))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.reset_index(drop=True))

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(a.reset_index())


# concat ya combine karna do ya usse jyada data frame ko

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# a1 = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(pd.concat([a,a1],axis=1))

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# a1 = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
#     "marks": [80, 70, 90, 60]
# })
# print(pd.concat([a,a1],axis=0))


# merge

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "marks": [80, 70, 90, 60],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# city= pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#      "marks": [80, 70, 90, 60],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# print(pd.merge(a,city,on="name"))

# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "marks": [80, 70, 90, 60],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# city= pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#      "marks": [80, 70, 90, 60],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# print(pd.merge(a,city))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "marks": [80, 70, 90, 60]
# })
# city= pd.DataFrame({
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# print(a.join(city))

# import pandas as pd
# a=pd.read_csv("student.txt")
# print(a)


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["A", "B", "C", "D"],
#     "marks": [80, 70, 90, 60],
#     "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
# })
# a.to_csv("student.txt")
# print(a)


# string operation

# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["name"].str.strip())

# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["name"].str.lstrip())


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["name"].str.rstrip())


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " AMAN "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["name"].str.lower())


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["name"].str.upper())


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["city"].str.replace("Delhi","chandigarh"))


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["city"].str.contains("Delhi"))


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["city"].str.startswith("D"))


# import pandas as pd
# a = pd.DataFrame({
#     "name": [" pushkar ", " rahul ", " aman "],
#     "marks": [80, 70, 90],
#     "city": ["Delhi", "Delhi", "Mumbai"]
# })
# print(a["city"].str.endswith("i"))


# import pandas as pd
# a = pd.DataFrame({
#     "name": ["Pushkar", "Rahul", "Aman"],
#     "marks": [85, 72, 91],
#     "city": ["Delhi", "Mumbai", "Delhi"]
# })
# a.to_excel("students.xlsx", index=False)
# print(a)

# from openpyxl import load_workbook
# from openpyxl.worksheet.table import Table, TableStyleInfo

# # Excel file open karo
# wb = load_workbook("students.xlsx")

# # Active sheet select karo
# ws = wb.active

# # Table banao
# table = Table(displayName="StudentTable", ref="A1:C4")

# # Table ka style
# style = TableStyleInfo(
#     name="TableStyleMedium2",
#     showFirstColumn=False,
#     showLastColumn=False,
#     showRowStripes=True,
#     showColumnStripes=False
# )

# table.tableStyleInfo = style

# # Sheet mein table add karo
# ws.add_table(table)

# # Save karo
# wb.save("students_table.xlsx")

# print("Excel Table successfully created!")


# import  pandas as pd
# a=pd.DataFrame({
#     "name" : ["pushkar","rahul","aman","rohit"],
#     "age" : [18,20,19,21],
#     "marks" : [85,72,91,65],
#     "city" : ["delhi","mumbai","delhi","mumbai"]
# })
# a["result"] = a["marks"].apply(
#     lambda x: "Pass" if x >= 80 else "Need Improvement"
# )
# print(a)
