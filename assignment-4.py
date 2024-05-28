'''Problem statement:
a) Write a Python program to store names and mobile numbers of your friends in
sorted order on names. Search your friend from list using binary search
(recursive and non- recursive). Insert friend if not present in phonebook
b) Write a Python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using Fibonacci search. Insert friend if not
present in phonebook.'''

N=[]
M=[]
def bubblesort():
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
	
bubblesort()
print(N)

print("Enter their mobile numbers acccording to sorted order: ")
for i in range(0,n):
	n2=int(input("enter number: "))
	M.append(n2)
print(M)
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


