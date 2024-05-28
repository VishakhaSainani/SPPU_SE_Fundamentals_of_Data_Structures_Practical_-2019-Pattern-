/*Problem statement:

Queues are frequently used in computer programming, and a typical example is the creation
of a job queue by an operating system. If the operating system does not use priorities, then
the jobs are processed in the order they enter the system. Write C++ program for simulating
job queue. Write functions to add job and delete job from queue.*/

#include<iostream>
using namespace std;
#define max 50
class Queue{
int front,rear;
int size;
int data[max];

public:
Queue(){
    front=rear=-1;
}
int isempty(){
    if(front==rear) return 1;
    return 0;
}
int isfull(){
    if(rear==max){
        return 1;
    }
    return 0;
}

void enqueue(int x){
    if(!isfull()){
    data[rear]=x;
    rear++;}
    else cout<<"queue is full";
}

void delqueue(){
int job;
job=data[front];
front++;
cout<<"Deleted job: "<<job;
}
void display(){
 int i;
 cout<<"\n";   
 for(i=front;i<rear;i++){
    cout<<data[i]<<" ";
 }
}
};

int main(){
    Queue obj;
    int ch,x;
    do{    cout<<"\n 1. insert job\n 2.delete job\n 3.display\n 4.Exit\n Enter your choice:";
	       cin>>ch;
	switch(ch)
	{  case 1: if (!obj.isfull())
		   {   cout<<"\n Enter data:";
			cin>>x;
			obj.enqueue(x);
		   }
	          else
		      cout<< "Queue is overflow";
	           break;
	   case 2: if(!obj.isempty())
                obj.delqueue();
		    else
			{   cout<<"\n Queue is underflow";  }
		    cout<<"\nremaining jobs :";
		    obj.display();
	           break;
	  case 3: if (!obj.isempty())
	        {  cout<<"\n Queue contains:";
		       obj.display();
	        }
	        else
		         cout<<"\n Queue is empty";
	       break;
	  case 4: cout<<"\n Exit";
        }
      }while(ch!=4);
return 0;
}