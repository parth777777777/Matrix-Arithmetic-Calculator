a_matrix = []
b_matrix = []

A_row = int(input("enter number of rows in A:"))
A_column = int(input("enter number of coloumns in A:"))

B_row = int(input("enter number of rows in B:"))
B_column = int(input("enter number of coloumns in B:"))

addition_resultant_matrix= [[0]* A_column for _ in range(A_row)]
product_matrix = [[0]*B_column for _ in range(A_row)]

compatible_for_addition = False
compatible_for_multiplication = False
solved = False

if (A_column == B_row):
    compatible_for_multiplication= True
if (A_row==B_row and A_column==B_column):
    compatible_for_addition=True
    
def print_matrix(matrix):
    for row in matrix:
        print(row)

def multiply():            
    for i in range(A_row):
        for j in range(B_column):
            for k in range(A_column):
                product_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]
    print("Matrix A multiplied by Matrix B : ",print_matrix(product_matrix))
    
def add():
    for i in range(A_row):
        for j in range(A_column):
            addition_resultant_matrix[i][j] = a_matrix[i][j] + b_matrix[i][j]
    print("Matrix A + Matrix B = ",print_matrix(addition_resultant_matrix))
            
def subtract():
    for i in range(A_row):
        for j in range(A_column):
            addition_resultant_matrix[i][j] = a_matrix[i][j] - b_matrix[i][j]
    print("Matrix A - Matrix B =",print_matrix(addition_resultant_matrix))
    
def operation(): 
    code = int(input("select operation :\nAdd A+B --0 \nSubtract A-B --1 \nMultiply AxB --2\nInput code of required operation : \n"))
    global solved
    if code==0:
        if compatible_for_addition:
            add()
            solved= True
        else:
            print("Matrices are not compatible for addition.")
    elif code ==1 :
        if compatible_for_addition:
            subtract()
            solved= True
        else:
            print("Matrices are not compatible for subtraction.")
    elif code==2 :
        if compatible_for_multiplication:
            multiply()
            solved = True
        else:
            print("Matrices are not compatible for multiplication.")
    else:
        print("Invalid code , Try again")

print("INPUT MATRICES : ") 

for i in range(A_row):
    row = []
    for j in range(A_column):
        print(f"Enter A[{i}][{j}]:")
        row.append(float(input()))
    a_matrix.append(row)
    
for i in range(B_row):
    row = []
    for j in range(B_column):
        print(f"Enter B[{i}][{j}]:")
        row.append(float(input()))

    b_matrix.append(row)

print("Provided matrices are:")
print("A =")
print_matrix(a_matrix)
print("B =")
print_matrix(b_matrix)
print("Can be added or subtracted:", compatible_for_addition)
print("Can be multiplied (AxB):", compatible_for_multiplication)


while not solved:
    if compatible_for_addition or compatible_for_multiplication :
        operation()