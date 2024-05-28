'''PROBLEM STATEMENT:
write a python program to store marks obtained by n students and perform following operations:
the average score of the class 
highest and lowest score of the class
count of students who are absent
display marks with highest frequency'''

class students:
	list=[]
	def __init__(self,n):
		self.n=n
	
	def add(self):
		i=0
		#for i in range(self.n):
		while(i!=self.n):
			marks=int(input("Enter marks one by one and enter -1 for absent students\n"))
			if(marks!=-1 and marks<0):
				print("Marks must be a positive integer or -1 for absenties please enter valid marks!!")
				
			else:
				self.list.append(marks)
				print(self.list)
				i=i+1
			
	def avg(self):
		sum=0
		j=0
		for i in self.list:
				j=j+1
				if(i!=-1):
					sum=sum+i
		average=sum/j
		print("Average score of the class is :",end=" ")
		print("{0:.2f}".format(average))
	def highest(self):
		max1=0
		for k in self.list:
			if(k>max1):
				max1=k
		print(" Maximum score is",max1)
	def lowest(self):
		min1=100
		for k in self.list:
			if(k!=-1):
				if(k<min1):
					min1=k
		print(" Minimum score is",min1)
	def absent(self):
		cnt=0
		for m in self.list:
			if(m==-1):
				cnt=cnt+1
		print("No of students absent are",cnt)

	def frequency(self):
		marks1=0
		cnt=0
		freq=0
		for i in range (0,self.n):
			if(self.list[i]!=-1):
				cnt=1
				for j in range(i+1,self.n):
					if(self.list[i]==self.list[j]):
						cnt=cnt+1
						
						if(cnt>=freq):
							freq=cnt
							marks1=self.list[i]
		if(marks1==0):
			print("All marks have single frequency ")
		else:
			print("Marks with highest frequency:",marks1)
		
n=int(input("Enter how many students marks you want to store: "))		

s1=students(n)
s1.add()
ch=int(input("\n1)Find Average score\n2)Find highest score\n3)Find lowest score\n4)Find number of absent students\n5)Find the score with highest frequency\n6)Exit\nEnter your choice: "))
while(ch!=6):
	if(ch==1):
		s1.avg()
	if(ch==2):
		s1.highest()
	if(ch==3):
		s1.lowest()
	if(ch==4):
		s1.absent()
	if(ch==5):
		s1.frequency()
	
	ch=int(input("\n1)Find Average score\n2)Find highest score\n3)Find lowest score\n4)Find number of absent students\n5)Find the score with highest frequency\n6)Exit\nEnter your choice: "))

	

