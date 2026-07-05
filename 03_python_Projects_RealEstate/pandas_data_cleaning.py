import pandas as pd
df=pd.read_csv("RealEstate-USA (1).csv")


#First 10 and last 10
print('head')
print(df.head(10))
print("Tail")
print(df.tail(10))


print("Types")
print(df.dtypes)


print("df_Info",df.info)

#Summary of Statistics of DataFrame using describe() method.

print("Summary of Statistics of DataFrame using Describe()method_")
print(df.describe())


#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.

print("Shape")
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column

print("one columns")
street=df["street"]
print("acess the name column df:")
print(street)



# access multiple columns

multiiple_columns=df[["street","acre_lot"]]
print("access multiple_columns:_____")
print(multiiple_columns)



"""There are four primary ways to select rows with .loc. These include:
Selecting a single row
Selecting multiple rows
Selecting a slice of rows
Conditional row selection"""



# Case 1 : using .loc - default case - starts here


"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""


#Select a Single Row using Loc----

print("loc______")
single_row=df.loc[1]
print("Select a single_row_____using loc")
print(single_row)

#Selecting a single column using .loc

print("Single Column____")

single_column5=df.loc[:1,"acre_lot"]
print(single_column5)


#selecting a multiple colummn using .loc

print("multiple_columns_______________")
multiple_column6=df.loc[:5,["acre_lot","street"]]
print(multiple_column6)

multiiple_columns7=df.loc[:,["acre_lot","street"]]
print(multiiple_columns7)



##Selecting a slice of columns using .loc
print("slice of column using loc_______")
second_row7 = df.loc[:1,'city':"street"]
print(second_row7)

#Combined row and column selection using .loc
print("COMBINED___")
combined_row_col=df.loc[df["city"]=="Yauco","bed":"city"]
print(combined_row_col)

#Select Multiple_Rows using Loc

multiple_rows=df.loc[[1,6]]
print("Select a Multiple_rows____usng loc")
print(multiple_rows)


#Selecting a slice of rows using .loc

slicing_rows1=df.loc[1:7]
print("select a slicing of rows using .loc_-")
print(slicing_rows1)


slice_rows3=df.loc[4:7]
print(slice_rows3)

#Conditional selection of rows using .loc

print("FILTERING_______________")
selecting_rows4=df.loc[df["city"]=="Yauco"]
print(selecting_rows4)

print("--Case 1 : using .loc - default case - ends here--")

print("CASE__02")

print("# Case 2 using__index.loc -start--here ")


df_index_col1=pd.read_csv("RealEstate-USA (1).csv",index_col="brokered_by")

print(df_index_col1)
print("dtype_______")
print(df_index_col1.dtypes)

print("INFO_____")

print(df_index_col1.info())

print("SIZE_________")
print(df_index_col1.size)

print("INDEX__")
print(df_index_col1.index)
print("SHAPE____")
print(df_index_col1.shape)


print("single row___using.loc")
print(df_index_col1.loc[52707])
print("select multiple rows__using .loc")
df_index_col2=df_index_col1.loc[[51202,109906]]
print(df_index_col2)



#Conditional selection of rows using .loc
print("selection or rows using.loc")
df_index_col4=df_index_col1.loc[df_index_col1["acre_lot"]==0.12]
print(df_index_col4)

#selecting a single rows using.loc
print("select single row slicing using .loc")
df_index_col5=df_index_col1.loc[:55906,"street"]
print(df_index_col5)
print("selcet multiple rows slicing using.loc")
df_index_col6=df_index_col1.loc[:,["city","acre_lot"]]
                                   
print(df_index_col6)



#Selecting a slice of columns using .loc
print("Slicing________")
index_col6=df_index_col1.loc[:1205,"city":"zip_code"]
print(index_col6)

print("slicing")
index_col7=df_index_col1.loc[df_index_col1["city"]=="Aguadilla","price":"zip_code"]



print(index_col7)

print("END__LOC")


#       START ILOC____________
print("Start Iloc-----")
print("Case#03___Iloc")
'''Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""
'''
#Selecting a single row using .iloc



print("single row using.iloc")

single_r=df.iloc[0]
print(single_r)

print("Multiple rows using.iloc")
in_col=df_index_col1.iloc[[1,3,5]]
print(in_col)

#Selecting a slice of rows using .iloc

print("Select a slicing or rows using.iloc")
ind_row2=df_index_col2.iloc[1:4,5]
print(ind_row2)

#Selecting a single column using .iloc

ind_col3=df.iloc[:,5]
print(ind_col3)


#Selecting multiple columns using .iloc


multiple_column8=df.iloc[:,[2,7]]
print(multiple_column8)

#Selecting multiple columns using .iloc

multiple_col=df.iloc[3:5,2:8]
print(multiple_col)



#Combined row and column selection using .iloc


row_col=df.iloc[[1, 3, 5],1:6]
print(row_col)



print("COMPLETE ILOC_________")



# Case 3 : Using .iloc - ends here






"""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""
import pandas as pd
df= pd.read_csv("RealEstate-USA (1).csv")
print(df)
# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)


# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
# delete age column

df.drop("prev_sold_date",axis=1,inplace=True)
print(df)
#df.drop(columns=["bed"],inplace=True)
#print(df)
#df.drop(columns=["house_size","state"],inplace=True)
#print(df)



#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
 #display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
df.rename(columns={"price":"Price"},inplace=True)
df.rename(mapper={"bed":"Quality_Bed","status":"Status_For_sale"})
print(df) 




# rename column one index label

print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")

df.rename(index={0: 7}, inplace=True)
df.rename(mapper={1: 10, 2:100},axis=0, inplace=True)
print(df)



#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

print("selected_rows.to_string()")


selecting_rows=df.query("city== \"peutro\" or Price > 89000")
print(selecting_rows)




# sort DataFrame by price in ascending order

sorted_df=df.sort_values(by="Price")
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Price', 'acre_lot'])
print(df1.to_string(index=False))
print("Sorting by 'price' (ascending) and then by 'location_id' (ascending):\n")



"""
 row before wrapping text."""



#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category



grouped = df.groupby('acre_lot')['Price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)



# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.

# to be continued....



df.drop_duplicates()
print(df)


df.fillna(0)
print(df)

# Save cleaned and modified DataFrame
df.to_csv("RealEstate-USA-1.csv", index=False)

print("CSV file saved successfully.")



