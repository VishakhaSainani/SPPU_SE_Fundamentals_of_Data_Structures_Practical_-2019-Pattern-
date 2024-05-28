/*Problem statement:

A palindrome is a string of character that‘s the same forward and backward. Typically,
punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a
droop” is a palindrome, as can be seen by examining the characters “poor danisina
droop” and observing that they are the same forward and backward. One way to check
for a palindrome is to reverse the characters in the string and then compare with
them the original-in a palindrome, the sequence will be identical. Write C++
program with functions-
a) To print original string followed by reversed string using stack
To check whether given string is palindrome or not*/


#include<iostream>
using namespace std;
#include<string.h>
#define max 50
using namespace std;
class s{
int top; char stack[50];
int size;
public:
s(){
top=-1; size=50;}
int pop();
void push(char);
void gettop();
int is_empty();
int is_full();
void reverse();
void convert (char[]);
void palindrome();

};

int s::is_empty(){
if(top==-1)
return 1;
else return 0;}

int s::is_full(){
if(top==size-1)
return 1;
else return 0;}

void s::gettop(){
if(!is_empty())
cout<<stack[top];
else cout<<"Stack is empty";}

void s:: push(char a){
if(!is_full()){
top++;
stack[top]=a;
stack[top+1]='\0';}

else{
cout<<"Overflow size";}
}

int s:: pop(){
if(!is_empty())
return stack[top--];
else{
cout<<"underflow state";
return -1;}}


void s::reverse()
{
	char str[max];
	
	cout<<"\n\nReverse string is : ";
		
	for(int i=top,j=0; i>=0; i--,j++)
	{
		cout<<stack[i];
		//str[j]=stack[i];
	}
	
	cout<<endl;
}


void s::convert(char str[])
{
	int j,k,len = strlen(str);

	for(j=0, k=0; j<len; j++)
	{
		if( ( (int)str[j] >= 97 && (int)str[j] <=122 ) || ( (int)str[j] >= 65 && (int)str[j] <=90 ))
		{
			if( (int)str[j] <=90 )
			{
				str[k] = (char)( (int)str[j] + 32 );
			}else
			{
				str[k] = str[j];				
			}

			k++;			
		}
	}
	str[k]='\0';

	cout<<endl<<"Converted String : "<<str<<"\n";
}




void s::palindrome()
{	
	char str[max];
	int i,j;		

	for(i=top,j=0; i>=0; i--,j++)
	{
		str[j]=stack[i];
	}
	str[j]='\0';
	
	
	if(strcmp(str,stack) == 0)
		cout<<"\n\nString is palindrome...";
	else
		cout<<"\n\nString is not palindrome...";
}

int main(){
    s s1;

	char str[max];
	int i=0;
	
	cout<<"\nEnter string to be reversed and check is it palindrome or not : \n\n";
	
	cin.getline(str , 50);
	
	s1.convert(str);
	
	while(str[i] != '\0')
	{
		s1.push(str[i]);
		i++;
	}
s1.reverse();
s1.palindrome();

	
}