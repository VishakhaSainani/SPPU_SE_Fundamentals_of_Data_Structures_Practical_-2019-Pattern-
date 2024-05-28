'''Problem statement:
Write a Python program to store second year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores'''


A=[]
n=int(input("Enter no. of students: "))
for i in range(0,n):
    a=float(input("Enter perentage: "))
    A.append(a)

def insertionsort():
    pass1=0
    for i in range(1,n):
        temp=A[i]
        j=i-1
        while(j>=0 and temp<A[j]):
            A[j+1]=A[j]
            j=j-1
        A[j+1]=temp
        pass1=pass1+1
        print("pass:",pass1,":-",A)

def shellsort():
    pass2=0
    gap=n//2
    
    while(gap>0):
        for i in range(gap,n):
            temp=A[i]
            j=i
            while(j>=gap and A[j-gap]>temp):
                A[j]=A[j-gap]
                j=j-gap
                #pass2=pass2+1
            A[j]=temp
        gap=gap//2
        pass2=pass2+1
        print("pass:",pass2,":-",A)

ch=int(input("Enter 1 for insertion sort and 2 for shell sort: "))

if(ch==1):
    insertionsort()
    print("\nSorted Array: ",A)
    i=n-1
    print("\nTop five scores: ")
    while(i!=n-6):
        print(A[i],end=" ")
        i=i-1

if(ch==2):
    shellsort()
    print("\nSorted Array: ",A)
    i=n-1
    print("\nTop five scores: ")
    while(i!=n-6):
        print(A[i],end=" ")
        i=i-1