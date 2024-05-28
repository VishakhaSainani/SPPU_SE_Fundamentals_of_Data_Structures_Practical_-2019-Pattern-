
'''Problem statement:
a) Write a Python program to store names and mobile numbers of your friends in
sorted order on names. Search your friend from list using binary search
(recursive and non- recursive). Insert friend if not present in phonebook
b) Write a Python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using Fibonacci search. Insert friend if not
present in phonebook.'''
 
N=[]
M=[]
def bubblesort(N):
    cnt=0
    for i in range(1,n-1):
        cnt+=1
        for j in range(0,n-cnt):
            if(N[j]>N[j+1]):
                temp=N[j]
                N[j]=N[j+1]
                N[j+1]=temp
		
n=int(input("Enter size for how many names you want to store: "))
for i in range(0,n):
	n1=input("Enter name: ")
	N.append(n1)
#N.sort()	
bubblesort(N)
print(N)


print("Enter their mobile numbers acccording to sorted order: ")
for i in range(0,n):
	n2=int(input("enter number: "))
	M.append(n2)
print(M)
def binarysearch():
	l1=0
	h1=n-1
	mid1=(l1+h1)//2
	flag=0
	cnt=0
	key=input("Enter the name you want to search: ")
	while(l1<=h1):
		
		if(N[mid1]==key):
		
			pos=mid1
			print("Position of name is: ",mid1+1)
			print("Number of comparisons: ",cnt+1)
			flag=1
			break
		
		if(N[mid1]>key):
			cnt=cnt+1
			h1=mid1-1
			mid1=(l1+h1)//2
			
		
		if(N[mid1]<key):
			cnt=cnt+1
			l1=mid1+1
			mid1=(l1+h1)//2



	if(flag!=1):
		print("Name not present ")
		print("Enter the name you want to add: ")
		name=input("Name: ")
		N.append(name)
		print("Enter the number: ")
		num=int(input())
		M.append(num)
		#n=n+1
		#bubblesort()
		print(N)
	#print(cnt)

def fibonaccisearch():
	
	key=int(input("Enter the number you want to search: "))
	f1=0
	flag=0
	f2=0
	f=f1+f2
	while(f<n):
		f2=f1
		f1=f
		f=f1+f2
	offset=-1
	while(f>1):
		i=min(offset+f2,n-1)

		if(key<M[i]):
			f=f2
			f1=f1-f2
			f2=f-f1
		elif(key>M[i]):
			f=f1
			f1=f2
			f2=f-f1
			offset=i
		else:
			flag=1
			print("Position of number is: ",i+1)

	if(f1 and M[n-1]==key):
			flag=1
			print("Position of number is: ",n)
	if(flag==0):
			print("Number not present!")

def fibMonaccianSearch(arr, x, n):
 
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
 
    # fibM is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
 
    # Marks the eliminated range from front
    offset = -1
 
    # while there are elements to be inspected.
    # Note that we compare arr[fibMm2] with x.
    # When fibM becomes 1, fibMm2 becomes 0
    while (fibM > 1):
 
        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)
 
        # If x is greater than the value at
        # index fibMm2, cut the subarray array
        # from offset to i
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
 
        # If x is less than the value at
        # index fibMm2, cut the subarray
        # after i+1
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
 
        # element found. return index
        else:
            return i
 
    # comparing the last element with x */
    if(fibMMm1 and arr[n-1] == x):
        return n-1
 
    # element not found. return -1
    return -1
ch=0		
print("1)Search for name(Binary search)\n2)Search for number(Fibonacci search)\n3)Exit")
while(ch!=3):
	ch=int(input("Enter choice: "))
	if(ch==1):
		binarysearch()
	if(ch==2):
		bubblesort(M)
		k=int(input("serach"))
		fibMonaccianSearch(M,n,k)
		


