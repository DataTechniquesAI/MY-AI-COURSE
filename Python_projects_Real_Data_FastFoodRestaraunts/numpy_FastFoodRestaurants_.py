import numpy as np
np.set_printoptions(threshold=np.inf,linewidth=np.inf)


address,latitude, longitude, name=np.genfromtxt("FastFoodRestaurants.csv",
                 delimiter=",",
                 usecols=(0,4,5,6),
                 skip_header=1,
                 unpack=True,
                 invalid_raise=False,
                 encoding="utf-8",
                 dtype=("U100","f8","f8","U100") )               

print("address",address)
print("latitude",latitude)
print(longitude)
print(name)
#Clean Nan values
print("Remove nan values__")
print("Latitude")
mask = ~np.isnan(latitude) &~ np.isnan(longitude)
latitude=latitude[mask]
longitude=longitude[mask]
name=name[mask]
address=address[mask]
print(longitude)
print(latitude)
print(name)
print(address)


#min,Max,Sum,Sub,Std
#Longitude

print(np.min(longitude))
print(np.max(longitude))
print(np.sum(longitude))
print(np.absolute(longitude))
print(np.absolute(longitude)) 
print(np.std(longitude))
print(np.average(longitude)) 
print(np.mean(longitude))
print(np.amin(longitude))
print(np.amax(longitude)) 
print(np.abs(longitude))
print(np.power(longitude,2))

#Latitude

print(np.min(latitude))
print(np.max(latitude))
print(np.sum(latitude))
print(np.absolute(latitude))
print(np.std(latitude))
print(np.average(latitude))
print(np.mean(latitude))
print(np.std(latitude))
print(np.amax(latitude))
print(np.amin(latitude))
print(np.abs(latitude))
print(np.power(latitude,2))
print(latitude.shape)
print(longitude.shape)

# Perform basic arithmetic operations

addition=longitude+latitude
subtraction=latitude-longitude
multiplication=latitude*longitude
division=latitude/ longitude


print("addition_lat+long",addition)
print("substraction_lat-lon",subtraction)
print("multiplication_lat*long",multiplication)
print("division_lat/long",division) 


#Trigonometric Functions
longitudepi=(longitude/np.pi)+1
sin_longitude=np.sin(longitude)
cos_longitude=np.cos(longitude)
tan_longitude=np.tan(longitude)


print(sin_longitude)
print(cos_longitude)
print(tan_longitude)

latitudepi=(latitude/np.pi)+1
sin_latitude=np.sin(latitude)
cos_latitude=np.cos(latitude)
tan_latitude=np.tan(latitude)

print(sin_latitude)
print(cos_latitude)
print(tan_latitude)

print(np.exp(longitude))
print(np.exp(latitude))


 #Calculate the natural logarithm and base-10 logarithm

log_array1=np.log(longitude)
log_array2=np.log(latitude)
print(log_array1)
print(log_array2)

log_array10=np.log10(longitude)
lod_array10=np.log10(longitude)
print(log_array10)
print(lod_array10)


# Calculate the hyperbolic sine of each element
sinh_values1 = np.sinh(longitude)
sinh_values2=np.sinh(latitude)

print(sinh_values1)
print(sinh_values2)

# Calculate the hyperbolic cosine of each element
cosh_values1=np.cosh(latitude)
cosh_values2=np.cosh(longitude)
print(cosh_values1)
print(cosh_values2)
tanh_values1=np.tanh(latitude)
tanh_values2=np.tanh(longitude)
print(tanh_values1)
print(tanh_values2)


 #Calculate the inverse hyperbolic sine of each element


arc_values1=np.arcsinh(longitude)
arc_values2=np.arcsinh(latitude)
print(arc_values1)
print(arc_values2)

#Long Plus Lat - 2 dimentional arrary

D2long_lat=np.array([longitude,latitude])
print(D2long_lat)



# check the dimension of array1
print(D2long_lat.ndim)

print(D2long_lat.size)

print(D2long_lat.shape)
print(D2long_lat.dtype)

# Slicing array


D2long_latslice=D2long_lat[1:0:1,1:5:1]#empty[]
D2long_latslice1=D2long_lat[:1,4:15:4]
print(D2long_latslice)
print(D2long_latslice1)

# Indexing array

D2long_latitemonly=D2long_lat[0,1]

print(D2long_latitemonly)

D2long_latitemonly1=(D2long_lat[0,4])
print(D2long_latitemonly1)


#You should use the builtin function nditer, if you don't need to have the indexes values.

for elem in np.nditer(D2long_lat):
    print(elem)
print(np.median(longitude))
print(np.median(latitude))

print(np.var(longitude))
print(np.var(latitude))
print(np.round,(latitude,2))
print(np.round(longitude,2))
print(np.floor(longitude))
print(np.floor(latitude))
print(np.ceil(latitude))
print(np.ceil(longitude))

print(np.maximum(latitude,longitude))
print(np.minimum(longitude,latitude))


print(np.sort(longitude)) 
print(np.sort(latitude))

print(np.unique(name))
print(np.count_nonzero(longitude)) 
print(np.count_nonzero(latitude))  

print(latitude>80) 
print(longitude< -80) 

print(np.cumsum(latitude))
print(np.cumprod(np.abs(latitude)))



print(D2long_lat.reshape(2,-1))
 
print(latitude[::-1])
print(longitude[::-1])  

 
for index ,value in np. ndenumerate(latitude):
    print(index,value)

 