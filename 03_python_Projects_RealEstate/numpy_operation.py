"""
NumPy Operations Project

This project demonstrates basic NumPy operations on a real estate dataset, including:
- Array slicing
- Square and square root
- Power calculations
- Absolute values
- Mathematical operations on data

Library: NumPy
"""
import numpy as np

data = np.genfromtxt(
    "RealEstate-USA (1).csv",
    delimiter=",",
    usecols=(2,3,5,6),
    skip_header=1,
    unpack=True
)

price,bed,acre_lot,street = data
price = price[~np.isnan(price)]
print(price)
bed =bed[~np.isnan(bed)]
print(bed)

print("Basic Operations:")

print("Square:", np.square(price[:10]))
print("Square Root:", np.sqrt(price[:10]))
print("Power 2:", np.power(price[:10], 2))
print("Absolute:", np.abs(price[:10]))

#min,Max,Sum,Sub,Std

print("min_price:",np.min(price))
print("max_price:",max(price))
print("Sub_price:",np.shape(price))
print("Add_price:",np.add(price,10))
print("std_price:",np.std(price))
print("mean_price:",np.mean(price))
print("Median_price:",np.median(price))
print("Operation Done")


# Percentiles
print("percentile")
print("percentiles_24th:",np.percentile(price,24))
print("percentile_56th:",np.percentile(price,54))
print("percentile_50th:",np.percentile(price,50))
print("percentile_100th:",np.percentile(price,100))


#array shape and size


print("size and shape")
print("size_price:",np.size(price))
print("shape_price:",np.shape(price))

#Index of Maximum And Minimum
print("Argmax_price:",np.argmax(price))
print("argmin_price:",np.argmin(price))


#Sorting 
print("sorting:",np.sort(price[:17]))

#Unique Values Count

print("Unique_count_price:",len(np.unique(price)))


# Slicing example
print("Slice:", price[3:15])


# Arrays 
print("Arrays Start")
print("array:",np.array(bed)[:10])

print("Arrange:",np.arange(10,20))
print("Linespace:",np.linspace(0,100,19))
print("Zeroes:",np.zeros(19))
print("Ones:",np.ones(10))
print("full:",np.full(10,15))


#Array Information
print("Array__Information")
print("shape_street",np.shape(street))
print("Size_acrelot",np.size(acre_lot))
print("Ndim:",np.ndim(street))
print("dtype:",price.dtype)
print("Itemsize:",street.itemsize)



#Reshaping

print("Reshaping_.........")
print("reshape",np.reshape(2,1))
print("transpose:",np.transpose(street))
#print("connect",np.concatenate(bed,street))

#print("Vertically_stack",np.vstack(price,street)[:5])
#print("Horizontally_stack:",np.hstack(bed,street)[:8])



#sample
sample = np.array([[1,2,3],[4,5,6]])
print(sample.transpose())
print(sample.flatten())




