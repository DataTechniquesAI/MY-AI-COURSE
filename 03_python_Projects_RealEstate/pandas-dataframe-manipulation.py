""""Pandas DataFrame Manipulation
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
df.drop(columns=["bed"],inplace=True)
print(df)
df.drop(columns=["house_size","state"],inplace=True)
print(df)



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


