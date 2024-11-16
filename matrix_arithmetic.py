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
    print("Matrix A multiplied by Matrix B : ")
    return print_matrix(product_matrix) 
def add():
    for i in range(A_row):
        for j in range(A_column):
            addition_resultant_matrix[i][j] = a_matrix[i][j] + b_matrix[i][j]
    print("Matrix A + Matrix B : ")
    return print_matrix(addition_resultant_matrix)
    
            
def subtract():
    for i in range(A_row):
        for j in range(A_column):
            addition_resultant_matrix[i][j] = a_matrix[i][j] - b_matrix[i][j]
    print("Matrix A - Matrix B :")
    return print_matrix(addition_resultant_matrix)

def transpose(matrix):
    rows= len(matrix)
    cols= len(matrix[0]) if rows > 0 else 0
    
    transposed_matrix = [[0] * rows for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            transposed_matrix[i][j] = matrix[j][i]
    print("Transpose of given matrix is : ")
    return print_matrix(transposed_matrix)   
    
def selection_prompt():
    global code 
    print("\nSelect operation :\n")
    print("Add A+B -- 0\n")
    print("Subtract A-B -- 1\n")
    print("Multiply AxB -- 2\n")
    print("Transpose a Matrix -- 3\n")
    code= int(input("Enter choice of code: "))
    
def ask_if_solved():
    global solved 
    check_if_done = str(input("close calculator and erase memory? "))
    if check_if_done=="Y" or check_if_done== "y":
        solved= True
    else :
        solved= False    
         
def operation(): 
    selection_prompt()
    if code==0:
        if compatible_for_addition:
            add()
            ask_if_solved()
        else:
            print("\nERROR : Matrices are not compatible for addition.")
            print("------------------------------------------------------------------------------")
            
    elif code ==1 :
        if compatible_for_addition:
            subtract()
            ask_if_solved()
        else:
            print("\nERROR : Matrices are not compatible for subtraction.")
            print("------------------------------------------------------------------------------")
            
    elif code==2 :
        if compatible_for_multiplication:
            multiply()
            ask_if_solved()
        else:
            print("\nERROR : Matrices are not compatible for multiplication.")
            print("------------------------------------------------------------------------------")
            
    elif code ==3:
        selection= str(input("Which matrix to transpose : A or B? "))
        if selection =="A" or selection== "a":
            transpose(a_matrix)
            ask_if_solved()
        elif selection == "B" or selection == "b":
            transpose(b_matrix)
            ask_if_solved()
        else:
            print("--------------Invalid input, try again.---------------")
        
    else:
        print("--------------Invalid code, try again.---------------")

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

print("\nProvided matrices are:")
print("A =")
print_matrix(a_matrix)
print("\nB =")
print_matrix(b_matrix)
print("\nCan be added or subtracted:", compatible_for_addition)
print("Can be multiplied (AxB):", compatible_for_multiplication)

while not solved:
        operation()