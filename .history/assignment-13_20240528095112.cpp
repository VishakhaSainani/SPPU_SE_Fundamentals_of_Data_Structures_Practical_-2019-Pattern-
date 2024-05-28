/*Problem statement:
A double-ended queue (deque) is a linear list in which additions and deletions may be made at
either end. Obtain a data representation mapping a deque into a one- dimensional array. Write
C++ program to simulate deque with functions to add and delete elements from either end of the
deque.*/

#include<iostream>
using namespace std;
#define max 5

class deque{
    int data[max]; int front,rear;
    public:
    deque(){front=rear=-1;}
bool isempty(){
    return front == -1 && rear == -1;
}
bool isfull(){
    return  (front == 0 && rear == max - 1) || (front == rear + 1) ;
}
   
void insertfront(int val){
        // checking if full
        if(isfull()){
            cout<<"Deque is full";
            return;
        }
        //if first element
        else if(isempty()){
            front=0;rear=0;
        }
        //maintaining cyclic nature
        else if(front==0)
        front=max-1;
        //normal flow
        else
        front--;

        data[front]=val;
        cout<<"Enqueued "<<val<<" to front";
    }

void insertrear(int val){
        //checking if full
        if(isfull()){
           cout << "DE-Queue is full"<<endl;
        return; 
        }
        // if first element
        else if(isempty()){
          front++;
          rear++;  
        }
        //maintain cyclic nature
        else if(rear==max-1){
            rear=0;
        }
        else
        rear++;

        data[rear]=val;
        cout<<"Enqueued "<<val<<" at rear";
        }

void deletefront(){
        int temp=data[front];
        //checking if empty
        if(isempty()){
            cout<<"Empty Queue";
            return;
            }
        //only one element present
        else if(front==rear)
           front=rear=-1;
            //maintaining cyclic nature
        else if(front==max-1)
           front=0;
           //normal
        else
           front++;
        cout<<"Dequed "<<temp<<" from front"<<endl;
        }

void deleterear(){
    int temp=data[rear];
    // if queue id empty
    if(isempty()){
            cout<<"Queue is empty"<<endl;
            return;
            }
    //only one element
    else if(front==rear){
            front=rear=0;
            }
            //cyclic nature
    else if(rear==0)
            rear=max-1;
            //normal flow
            else rear--;
            cout<<"Dequed "<<temp<<" from queue"<<endl;
        }

    void display(){
        if(isempty()){
                cout<<"Deque is empty";
                return;
            }
            cout<<"Deque is: ";

        for(int i=front;i!=rear;i=(i+1)%max)
            cout<<data[i]<<" ";
            cout<<data[rear];
            cout<<endl;
        }
};
int main(){
            deque d1;
            int x,ch;
            while(true){
                 cout << endl
             << "    DE-QUEUE OPERATIONS    " << endl
             << endl
             << "1-Insert At Front" << endl
             << "2-Insert At Rear" << endl
             << "3-Delete From Front" << endl
             << "4-Delete From rear" << endl
             << "5-Display" << endl
             << "0-Exit" << endl;
        cout << " ==>your choice ";
        cin >> ch;
        cout << endl;

        switch(ch){
            case 1:
            cout<<"Enter data: ";
            cin>>x;
            d1.insertfront(x);
            break;
            case 2:
            cout<<"Enter data: ";
            cin>>x;
            d1.insertrear(x);
            break;
            case 3:
            d1.deletefront();
            break;
            case 4:
            d1.deleterear();
            break;
            case 5:
            d1.display();break;
            case 0:
            cout<<"Exited!";
            goto a;
            break;

        }
            }
     a: return 0;   }
