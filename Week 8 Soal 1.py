from array import array
data_list = [100, 200, 300, 400]
data_array = array('i',[10,20,30,40])

data_list.append(500)
data_array.append(50)

data_list[0] = "Seratus"
data_array[0] = 100

print("Data List :", data_list)
print("Data Array:", data_array)