'''Problem Statement:
write a python program to compute following computation on matrix
a) Addition of two matrices b)Subtraction of two matrices c)Multiplication of two matrices d) transpose of matrix

'''
   
def addition_matrix():
    A1 = []
    r1 = int(input("enter the number of rows for first matrix: "))
    c1 = int(input("enter the number of coloums for first matrix: "))
    for i in range(0,r1):
        A = []
        for j in range(0,c1):
            n = int(input("enter the elements: "))
            A.append(n)
        A1.append(A)
    #to print matrix
    for i  in range(r1):
        for j in range(c1):
            print(A1[i][j],end = " ")
        print()
    B1 = []
   
    r2 = int(input("enter the number of rows for second matrix: "))
    while(r1!=r2):
       
        r2 = int(input("enter the equal number of rows to perform addition: "))
        if(r1 == r2):
            break
    c2 = int(input("enter the number of coloums for second matrix: "))
    while(c1!=c2):
       
        c2 = int(input("enter the equal number of coloms to perform addition: "))
        if(c1 == c2):
            break
    for i in range(0,r2):
        B = []
        for j in range(0,c2):
            n = int(input("enter the elements: "))
            B.append(n)
        B1.append(B)
    #to print matrix
    for i  in range(r2):
        for j in range(c2):
            print(B1[i][j],end = " ")
        print()
    if(r1 == r2 and c1 ==c2):
        ADD1 = []
        for i in range(0,r2):
            ADD = []
            for j in range(0,c2):
                ADD.append(A1[i][j]+B1[i][j])
            ADD1.append(ADD)
        print("***ADDED MATRIX***")
        for i in range(r2):
            for j in range(c2):
                print(ADD1[i][j],end = " ")
            print()
       
def subtraction_matrix():
    A1 = []
    r1 = int(input("enter the number of rows for first matrix: "))
    c1 = int(input("enter the number of coloums for first matrix: "))
    for i in range(0,r1):
        A = []
        for j in range(0,c1):
            n = int(input("enter the elements: "))
            A.append(n)
        A1.append(A)
    #to print matrix
    for i  in range(r1):
        for j in range(c1):
            print(A1[i][j],end = " ")
        print()
    B1 = []
   
    r2 = int(input("enter the number of rows for second matrix: "))
    while(r1!=r2):
       
        r2 = int(input("enter the equal number of rows to perform subtraction: "))
        if(r1 == r2):
            break
    c2 = int(input("enter the number of coloums for second matrix: "))
    while(c1!=c2):
       
        c2 = int(input("enter the equal number of coloms to perform subtraction: "))
        if(c1 == c2):
            break
    for i in range(0,r2):
        B = []
        for j in range(0,c2):
            n = int(input("enter the elements: "))
            B.append(n)
        B1.append(B)
    #to print matrix
    for i  in range(r2):
        for j in range(c2):
            print(B1[i][j],end = " ")
        print()
    if(r1 == r2 and c1 ==c2):
        ADD1 = []
        for i in range(0,r2):
            ADD = []
            for j in range(0,c2):
                ADD.append(A1[i][j]-B1[i][j])
            ADD1.append(ADD)
        print("***SUBTRACTED MATRIX***")
        for i in range(r2):
            for j in range(c2):
                print(ADD1[i][j],end = " ")
            print()

def multiplication_matrix():
    A1 = []
    r1 = int(input("enter the number of rows for first matrix: "))
    c1 = int(input("enter the number of coloums for first matrix: "))
    for i in range(0,r1):
        A = []
        for j in range(0,c1):
            n = int(input("enter the elements: "))
            A.append(n)
        A1.append(A)
    #to print matrix
    for i  in range(r1):
        for j in range(c1):
            print(A1[i][j],end = " ")
        print()
    B1 = []
   
    r2 = int(input("enter the number of rows for second matrix: "))
    while(c1!=r2):
       
        r2 = int(input("enter the value equal to coloum of first matrix to perform multiplication: "))
        if(c1 == r2):
            break
    c2 = int(input("enter the number of coloums for second matrix: "))
   
    for i in range(0,r2):
        B = []
        for j in range(0,c2):
            n = int(input("enter the elements: "))
            B.append(n)
        B1.append(B)
    #to print matrix
    for i  in range(r2):
        for j in range(c2):
            print(B1[i][j],end = " ")
        print()
    mul = []
    if(c1 == r2):
        for i in range(0,r1):
            mul1 = []
            for j in range(0,c2):
                mul1.append(0)
            mul.append(mul1)
        for i in range(0,r1):
            mul2 = []
            for j in range(0,c2):
                for k in range(0,c1):
                    mul[i][j] = mul[i][j]+A1[i][k] * B1[k][j]
                    mul2.append(mul)
                mul.append(mul2)
    print("****MATRIX MULTIPLICATION****")
    for i in range(0,r1):
        for j in range(0,c2):
            print(mul[i][j],end = " ")
        print()
    print("\n")

def transpose_matrix():
   
    A1 = []
    r1 = int(input("enter the number of rows for first matrix: "))
    c1 = int(input("enter the number of coloum for first matrix: "))
    for i in range(0,r1):
        A = []
        for j in range(0,c1):
            n = int(input("enter the elements: "))
            A.append(n)
        A1.append(A)
    #to print matrix
    for i  in range(r1):
        for j in range(c1):
            print(A1[i][j],end = " ")
        print()
    trans = []
    for j in range(c1):
        tran1 = []
       
        for i in range(r1):
            tran1.append(A1[i][j])
        trans.append(tran1)
    print("***TRANSPOSE MATRIX****")
    print(trans)
    
while True:  
    print("\n********MAIN MENU*******")  
    print("1. To perform addition of matrix")  
    print("2. to perform subtraction of matrix")
    print("3. To perform multiplication of matrix")
    print("4. To perform transpose of matrix")
   
    print("5. Exit")  
    choice1 = int(input("Enter the Choice:"))
   
    if choice1 ==1:
        addition_matrix()
    elif choice1 ==2:
        subtraction_matrix()
    elif choice1 == 3:
        multiplication_matrix()
    elif choice1 == 4:
        transpose_matrix()
    elif choice1 == 5:
        break
    #elif choice1 == 6:
     #   break
   
    else:
        print("OOPs! please enter a valid choice")