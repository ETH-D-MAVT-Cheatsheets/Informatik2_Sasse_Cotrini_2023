climate["jan"][3] #Access single element
climate["feb"] #Access single column (type: Series)
climate[["jan", "mar"]] #multiple columns (Dataframe)
climate.iloc[3] #Access single row (Series)
Climate.iloc[1:4] #multiple rows (Dataframe)
climate.iloc[4:7,1:2] #Access subtable (Dataframe)
#gets rows 4,7 with data only from column 1
#Access subtable using index column values and column name (Dataframe)
climate2 = climate.set_index("time")
climate2.loc[1864:1868,"jan":"mar"]
#includes the rows labeled with 1864 until and including #1868, the columns from "jan" until and including "mar"
