import numpy as np
'''
# numpy library

import numpy as np

threeD_arr = np.array([[[1,2,3],[4,5,6]], [[10,20,30],[40,50,60]]])

print(threeD_arr[0][0][0])
print(threeD_arr.ndim)
'''
'''
array1 = np.array([1,2,3])
array2 = np.array([7,8,9])

array3 = array1 + array2
array4 = array1 * array2
array5 = np.dot(array1, array2)

print(array3)
print(array4)
print(array5)
'''
'''
data = np.array([10,40,20,30])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", std_dev)
'''

# Pandas library
import pandas as pd
'''
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print(df.iloc[0,1])     # indexing
print(df.iloc[:, 0:1])      # slicing
print(df.loc[:,["calories", "duration"]])
'''
'''
data = {
    'Region': ['east', 'west', 'east', 'west', 'north', 'east', 'north'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'B', 'B'],
    'Sales': [500, 700 ,800, 600, 750, 900, 650]
}

df = pd.DataFrame(data)
print(df)
# It will group region first and the product and then show sum 
grouped_df = df.groupby(['Region', 'Product'])['Sales'].sum()
print(grouped_df,"\n")
'''
'''
df1 = pd.DataFrame({
    'ID': [1,2,3,4],
    'Name': ['ALice', 'Bob', 'Charlie', 'David'],
    'Dept': ['HR', 'IT', 'Finance', 'IT']
})

df2 = pd.DataFrame({
    'ID': [3,4,5,6],
    'Salary': [60000,50000,70000,80000]
})

print(df1)
print(df2)

# Using join we can combine these dataframes but there should at least one column to be common in both dataframes.
# inner join
inner_join = df1.merge(df2, on="ID", how="inner")
print("Inner Join: ", inner_join)

# left join
left_join = df1.merge(df2, on="ID", how="left")
print("Left Join: ", left_join)

# right join
right_join = df1.merge(df2, on="ID", how="right")
print("Right Join: ", right_join)

# Outer join
outer_join = df1.merge(df2, on="ID", how="outer")
print("Outer Join: ", outer_join)
'''

# Plots in python

import matplotlib.pyplot as plt
'''
xpoints = np.array([0,6])
ypoints = np.array([5,11])

plt.plot(xpoints, ypoints)
plt.show()

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph title")
'''

# Scatter plot

'''
x = np.array([2,3,5,7,8,9,4])
y = np.array([12,34,46,34,23,34,42])

plt.scatter(x, y)
plt.show()
'''

# Bar Graph
'''
x = ["A", "B", "C", "D"]
y = [2,5,7,9]
plt.bar(x, y)
plt.show()
'''

# Histogram
'''
x = np.random.normal(170, 10, 250) # getting numbers randomly

plt.hist(x)
plt.show()
'''

# Pie Chart

y = np.array([5,15,25,35])
mylabels = ["apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

