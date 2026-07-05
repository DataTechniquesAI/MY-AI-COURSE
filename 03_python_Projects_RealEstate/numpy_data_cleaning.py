import numpy as np

# Load required columns
data= np.genfromtxt(
    "RealEstate-USA (1).csv",
    delimiter=",",
    usecols=(2, 3, 4, 9),
    skip_header=1,
    unpack=True
)

price, bed, bath, zip_code = data
print(data)
# Clean NaN values
clean_price = price[~np.isnan(price)]
clean_bed = bed[~np.isnan(bed)]
clean_bath = bath[~np.isnan(bath)]
clean_zip = zip_code[~np.isnan(zip_code)]

print("Clean Data Summary:")
print("Price samples:", clean_price[:10])
print("Beds samples:", clean_bed[:10])
print("Bath samples:", clean_bath[:10])
print("Zip samples:", clean_zip[:10])

#Count Missing Values:
print("Missing_values:",np.isnan(price).sum())
print("Missing_values:",np.isnan(bed).sum())
print("Missing_values:",np.isnan(zip_code).sum())


#unique_Beds,zip_code

print("Unique_beds:",np.unique(clean_bed))
print("Unique_Zip_code:",np.unique(clean_zip))

#sorted
sorted_price=np.sort(price)
print(sorted_price[:9])


#Nanmax , nan minimum
print("")
print("Minimum_price:",np.nanmin(price))
print("Maximum_price:",np.nanmax(price))
print("sum_price:",np.nansum(price))
print("Mean_price:",np.nanmean(price))
print("median_price:",np.nanmedian(price))
print("var_price:",np.nanvar(price))


#Replace Nan with 0
print("replace Nan with 0")
bed_filled=np.nan_to_num(bed,nan=0)
print(bed_filled[4:])


#Find invalid Values
print("Any Nan left",np.isnan(price).any())

import numpy as np 
df=np.genfromtxt("RealEstate-USA (1).csv",
                 skip_header=1,unpack=True,delimiter=",")
print(df)


