import pandas as pd

pd.set_option("display.max_columns",None)

df=pd.read_csv("FastFoodRestaurants.csv")
print(df)

print(df.columns)
print(df)
print(df.head(5))
print(df.tail(7))
print(df.info())
print(df.describe())


#Missing value checks

print(df.isnull().sum())


#Remove duplicates

df.drop_duplicates(inplace=True)
print(df)

print(df.dtypes)
#Extra spaces remove
df["address"]=df["address"].str.strip()
df["city"]=df["city"].str.strip()
df["province"]=df["province"].str.strip()
df["websites"]=df["websites"].str.strip()
df["postalCode"]=df["postalCode"].str.strip()
df["province"]=df["province"].str.strip()
df["name"]=df["name"].str.strip()
df["country"]=df["country"].str.strip()
df["keys"]=df["keys"].str.strip()

print(df)

#Website fill
df["websites"]=df["websites"].fillna("Not Available")
df.fillna("pending")
print(df)


df["city"]=df["city"].str.title()
df["address"]=df["address"].str.title()
df["province"]=df["province"].str.title()
print(df)


df.rename(columns={"city":"City",
                   "address":"Address",
                   "province":"Province",
                   "websites":"Website",
                   "postalCode":"Postal_Code",
                   "latitude":"Latitude",
                   "name":"Name",
                   "longitude":"Longitude",
                   "country":"Country"},inplace=True)
print(df)


print("Longitude_max",df["Longitude"].max())
print("Longitude_mean",df["Longitude"].mean())
print("Longitude_sum",df["Longitude"].sum())



print("Latitude_max", df["Latitude"].max())
print("Latitude_mean",df["Latitude"].mean())
print("Latitude_sum",df["Latitude"].sum())

print(df.shape)
print(df.dtypes)
print("Unique_City")                  
print(df["City"].unique())
print(df["City"].nunique())
print("City ")
print(df["City"].value_counts())


print(df.columns.tolist())


df.sort_values(by="Name",ascending=True,inplace=True)
print(df)
print(df.isnull().sum().sum())



df.to_csv("FastfoodRestaraunt_cleaning_Pandas.csv",index=False)