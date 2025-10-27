A = [
    [
        [1,2,3], 
        [4,5,6]
    ],     
    [
        [7,8,9],
        [10,11,12]
    ]
]
print(A[0])

for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"Lapisan {i},Baris {j} -> {A[i][j][-1]}")    
