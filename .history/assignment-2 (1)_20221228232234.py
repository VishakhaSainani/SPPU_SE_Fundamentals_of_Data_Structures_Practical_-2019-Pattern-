def longest_word():
    str1=input("Enter a string\n")
    cnt = 0
    wd=""
    mwd=""
    mcnt=0
    for i in str1:
        if(i!= " "):
            cnt = cnt +1
            wd = wd + i
            if(cnt>mcnt):
                mcnt = cnt
                mwd = wd
        else:
            cnt = 0
            wd = " "
    print("Longest length word is: ",mwd)
   
def frequency():
    str1=input("Enter a string\n")
    count = 0
    maxcount = 0
    maxfreq = ""
    for i in str1:
        count = 0
        for j in str1:
            if(i==j):
                count = count +1
        if(count>maxcount):
            maxcount = count
            maxfreq = i
    print("highest occurence letter in the string is: ",maxfreq)
    print("frequency of highest occurence letter is: ",maxcount)
           
def palindrome():
    str1=input("Enter a string\n")
    newstr = ""
    for i in str1:
        newstr = i+newstr
    if(newstr == str1):
        print("given string is palindrome")
    else:
        print("given string is not palindrome")
       
'''def sub_String():
    str1=input("Enter a string\n")
    substr=input("enter substring\n")
    count1=0
    index=0
    m=str1.split()
    if substr in str1:
        a = substr[0]
        if substr in m:
            b = str1.index(a)
    print("index of first occurence of substring is",b)'''
def sub_String():
    str1=input("Enter a string\n")
    st = input("Enter substring:")
    c = str1.split(" ")
    b=str1.index(st)
    print("index of first occurence of substring is",b)
    for i in range(0,len(c)):
        if(st == c[i]):
          b=str1.index(st)
    print("index of first occurence of substring is",b)
def count_word():
    str1=input("Enter a string\n")
    st = input("Enter a word:")
    c = str1.split(" ")
    counter = 0
    for i in range(0,len(c)):
        if(st == c[i]):
            counter += 1
   
    print("occurence of the word ",st,"is: ",counter)
   


while True:  
    print("\n********MAIN MENU*******")  
    print("1. To display the word with longest length")  
    print("2. to determine the frequency of occurences of particular charecter in string")
    print("3. To check whether the given string is palindrome or not")
    print("4.To display index of the first appearance of the substring")
    print("5.To count the occurence of each word in a given string")
    print("6. Exit")  
    choice1 = int(input("Enter the Choice:"))
   
    if choice1 ==1:
        longest_word()
    elif choice1 ==2:
        frequency()
    elif choice1 == 3:
        palindrome()
    elif choice1 == 4:
        sub_String()
    elif choice1 == 5:
        count_word()
    elif choice1 == 6:
        break
   
    else:
        print("OOPs! please enter a valid choice")
       
       