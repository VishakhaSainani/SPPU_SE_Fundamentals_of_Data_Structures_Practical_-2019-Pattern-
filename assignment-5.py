'''
Assignment No.05
Problem Statement:
Write a Python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.'''



A=[]
n=int(input("Enter no. of students:"))
for i in range(0,n):
    a=float(input("Enter perentage "))
    A.append(a)

def bubblesort():
    cnt=0
    pass1=0
    for i in range(1,n):
        cnt+=1
        for j in range(0,n-cnt):
            if(A[j]>A[j+1]):
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
        pass1=pass1+1
        print("pass:",pass1,":-",A)
#another way
'''def selectionsort():
    pass2=0
    for i in range(0,n):
        minpos=i
        for j in range(i+1,n):
            if(A[j]<A[minpos]):
                minpos=j
        if(minpos!=1):
            temp=A[i]
            A[i]=A[minpos]
            A[minpos]=temp
        pass2=pass2+1
        print("pass:",pass2,":-",A)'''

def selectionsort():
    pass2=0
    for i in range(0,n-1):
        minpos=i
        for j in range(i,n):
            if(A[j]<A[minpos]):
                minpos=j
        
        temp=A[i]
        A[i]=A[minpos]
        A[minpos]=temp
        pass2=pass2+1
        print("pass:",pass2,":-",A)



ch=int(input("Enter 1 for buble sort and 2 for selection sort: "))
if(ch==1):
    print()
    bubblesort()
    print()
    print("Sorted array:")
    print(A)
    print()
    print("Top five scores:")
    
    i=n-1
    while(i!=n-6):
        print(A[i],end=" ")
        i=i-1
if(ch==2):
    print()
    selectionsort()
    print()
    print("Sorted array:")
    print(A)
    print()
    print("Top five scores:")
    i=n-1
    while(i!=n-6):
        print(A[i],end=" ")
        i=i-1

