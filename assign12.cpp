/*Problem statement:
Pizza parlor accepting maximum M orders. Orders are served in first come first served basis.
Order once placed cannot be cancelled. Write C++ program to simulate the system using
circular queue using array*/


#include<iostream>
using namespace std;
class circularqueue{
    int data; int front,rear; int size; int *arr;
    public:
    circularqueue(int s)
    {front=rear=-1; size=s; arr=new int[s];}
    void enqueue(int d){//checking if full
        if((front==0 && rear==size-1) || rear==(front-1)%(size-1)){cout<<" Ordering Queue is full"; return;}
       //first element insertion
        else if(front==-1){front=rear=0; arr[rear]=d; }
        //rear at end-to maintain cyclic nature
        else if(rear==size-1 && front!=0){rear=0; arr[rear]=d;}
        else{
            rear++;
            arr[rear]=d;
        }
    }

    int delqueue(){ int data=arr[front];arr[front] = -1;
        //checking if empty
        if(front==-1){cout<<"No orders placed!"; return 0;}
        //checking if only one element
        else if(front==rear){front=rear=-1;}
         //checking if front at end-to maintain cyclic nature
        else if(front==size-1){front=0;}
        else {front++;}
        cout<<"Serving order no.: "<<data<<endl; return data;
    }

    void display(){
        if(front==-1){cout<<"No orders in queue!"; return;}
        cout<<" Total Orders Preparing: ";
        if(rear>=front){
            for(int i=front;i<=rear;i++){
                cout<<arr[i]<<" ";
            }
        }
        else{
            for(int i=front;i<size;i++){
                cout<<arr[i]<<" ";
            }
            for(int i=0;i<=rear;i++){
                cout<<arr[i]<<" ";
            } 
        }cout<<endl;
    }
};

int main(){
    int ord,ch,bill=0;
    int n;
    n=5;
    circularqueue c(n);
    while(true){
        cout<<"Welcome to Vishakha's Pizza Parlour!"<<endl;
       
        cout<<"We accept maximum 5 orders at once and we follow first come first serve basis so please do wait and enjoy!!"<<endl;
       a: cout<<"\n1)Place order\n2)Serve Order\n3)Display Orders Placed\n4)Get Bill\n5)Exit!\nEnter choice: "; cin>>ch;
        switch(ch){
            case 1: cout<<"\n****************MENU****************"<<endl;
        cout<<"\n1)Veggies Pizza-Rs.100\n2)Seven Cheese Pizza-Rs.-170\n3)Margherita Pizza-Rs.140\n4)Pepperoni Pizza-Rs.130\n5)Chicago-style Pizza-Rs.150\n6)Paneer Pizza-Rs.160\nEnter choice: ";
        cin>>ord;
        switch(ord){
            case 1: 
            cout<<"Your order of Veggies Pizza is placed!<<"<<endl; bill=bill+100; c.enqueue(1);goto a;
            case 2:cout<<"Your order of Seven Cheese Pizza is placed!<<"<<endl; bill=bill+170;c.enqueue(2); goto a;
            case 3:cout<<"Your order of Margherita Pizza is placed!<<"<<endl; bill=bill+140;c.enqueue(3); goto a;
            case 4:cout<<"Your order of Pepperoni Pizza is placed!<<"<<endl; bill=bill+130; c.enqueue(4);goto a;
            case 5:cout<<"Your order of Chicago-style Pizza is placed!<<"<<endl; bill=bill+150; c.enqueue(5);goto a;
            case 6:cout<<"Your order of Paneer Pizza is placed!<<"<<endl; bill=bill +160; c.enqueue(6);goto a;
        }
        case 2://cout<<"Here's your order no.: ";
        c.delqueue(); goto a;
        case 3: c.display(); goto a;
        case 4:cout<<"Your total bill is Rs."<<bill;
        bill=0; goto a;
        case 5:cout<<"Thankyou ,do visit us again!"; goto m;
        }
    }
m: return 0;
}
