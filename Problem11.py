#In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
import numpy as np

filename = 'matrix.txt'

#store every line in an array
with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

# convert the strings into number integers
intArray = []
for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    intArray.append(k)

#convert array to matrix
main_matrix = np.matrix(intArray)
maxProd=0
for i in range(16):
    for j in range(16):
        prod1 = main_matrix[i,j]*main_matrix[i+1,j]*main_matrix[i+2,j]*main_matrix[i+3,j]
        if prod1 > maxProd:
            maxProd = prod1
        prod2 = main_matrix[i,j]*main_matrix[i,j+1]*main_matrix[i,j+2]*main_matrix[i,j+3]
        if prod2 > maxProd:
            maxProd = prod2
        prod3 = main_matrix[i,j]*main_matrix[i+1,j+1]*main_matrix[i+2,j+2]*main_matrix[i+3,j+3]
        if prod3 > maxProd:
            maxProd = prod3
        prod4 = main_matrix[19-i,j]*main_matrix[18-i,j+1]*main_matrix[17-i,j+2]*main_matrix[16-i,j+3]
        if prod4 > maxProd:
            maxProd = prod4
print (maxProd)
