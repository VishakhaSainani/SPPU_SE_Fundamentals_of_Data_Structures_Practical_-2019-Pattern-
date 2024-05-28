/*Problem Statement:
Department of Computer Engineering has student&#39;s club named &#39;Pinnacle Club&#39;.
Students of second, third and final year of department can be granted membership
on request. Similarly one may cancel the membership of club. First node is
reserved for president of club and last node is reserved for secretary of club. Write
C++ program to maintain club member‘s information using singly linked list. Store
student PRN and Name. Write functions to:
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club
c) Display members
d) Two linked lists exists for two divisions. concatenate two lists.*/

#include<iostream>
using namespace std;
#include<string>
class node{public:
    int data; string name; node* next;
};
class list{public:
    node *head,*temp;
    list(){ head=NULL;}
    node* create(){
        node *temp=new node; int value; string n;
        if(temp==NULL){cout<<"Memory not allocated"; return 0;}
        else{
            cout<<"Enter student PRN: "; cin>>value;
            cout<<"Enter student name: "; cin>>n;
            temp->data=value;
            temp->name=n;
            temp->next=NULL;
            return temp;
        }
    }

    node* allot(int value,string n){
        node *temp=new node; 
        if(temp==NULL){cout<<"Memory not allocated"; return 0;}
        else{
           
            temp->data=value;
            temp->name=n;
            temp->next=NULL;
            return temp;
        }
    }

    void insert_at_head(){
        node *temp=create();
        if(temp==NULL){
            head=temp;
            head->next=NULL;
         
        }
        else{
            temp->next=head;
            head=temp;
            
        }
        cout<<"President Updated!"<<endl;
    }
    void print(){
        node *s;
        s=head;
        while(s->next!=NULL){
            cout<<s->data<<" "<<s->name<<" ";
            s=s->next;
        }   cout<<s->data<<" "<<s->name<<endl;
    }
    void insert_at_tail(){
        node *temp=create();
        node *s; s=head;
        while(s->next!=NULL){
            s=s->next;
        } temp->next=NULL;
        s->next=temp;
       
        cout<<"Secretary updated!"<<endl;
    }
    int total(){
        int cnt=0; node* temp; temp=head;
        while(temp!=NULL){cnt++; temp=temp->next;}
        return cnt;
    }

    void insert_between(){
        node* temp; int pos,cnt=1;
        cout<<"Enter position at which the member is to be added: ";
        cin>>pos;
        temp=head;
        if(pos==1){insert_at_head(); return;}
        else if(pos<=total()){
            while(cnt<pos-1){
              
                temp=temp->next;  cnt++;
            }
        if(temp->next==NULL){insert_at_tail(); return;}
        node *node_to_be_inserted=create();
        node_to_be_inserted->next=temp->next;
        temp->next=node_to_be_inserted;
        cout<<"Member inserted!"<<endl; return;
        }
        cout<<"Position out of range!";
    }

    void delete_pos(int pos){
        node *current,*prev;
        int cnt=1; current=head;
        if(pos==1){ current=head; head=head->next;
        current->next=NULL; delete current; cout<<"President Deleted!";return;}
        else if(pos<=total()){ prev->next=NULL;
            while(cnt<pos){
            prev=current; current=current->next;
            cnt++;
        } prev->next=current->next;
        current->next=NULL;
        delete current;
        if(pos==total()){cout<<"Secretary deleted!"; return;}
        cout<<"Member deleted!"; return;
        }
        cout<<"Position out of range!"<<endl;
    }
    
    void merge(list A,list B){
         struct node* last; node* t;
        t=A.head;
        while(t!=NULL){
            int val=t->data; string s=t->name;
            temp=allot(val,s);
            if(head==NULL){
                head=temp;
                head->next=NULL;
                last=head;
            }
            else{
                last->next=t;
                last=t;
            }
            t=t->next;
        }
        last->next=B.head;
        t=B.head;
        while(t!=NULL){
            int val=t->data;
            string s=t->name;
            temp=allot(val,s);
            last=temp->next;
            last=temp;
            t=t->next;
        }
        last->next=NULL;
    }
    void update(){
        int val,pos,i; string sn;
        if(head==NULL){cout<<"List is empty!"; return;}
        cout<<"Enter position to be update: "; cin>>pos;
        cout<<"Enter new PRN: "; cin>>val;
        cout<<"Enter new name: "; cin>>sn;
        node *s,*ptr;
        s=head;
        if(pos==1){head->data=val; head->name=sn;}
        else{
            for(i=1;i<pos;i++){
                if(s==NULL){cout<<"There are less than"<<pos<<"elements";
                return;}
                s=s->next;
            }
            s->data=val; s->name=sn;
        }
        cout<<"Node Updated"<<endl;
    }

    void search(){
        int val,pos=0,flag=0;
        if(head==NULL){cout<<"empty!"<<endl; return;}
        cout<<"Enter student PRN to be searched: ";
        cin>>val;
        node *s;
        s=head;
        while(s!=NULL){
            pos++;
            if(s->data==val){flag=1; cout<<"Member is at position: "<<pos<<endl;}
            s=s->next;
        }
        if(!flag){cout<<"Member not present"<<endl;}
    }

    void reverse(){
        node *p1,*p2,*p3;
        if(head==NULL){cout<<"List is empty!"<<endl; return;}
        if(head->next==NULL){return;}
        p1=head;
        p2=p1->next;
        p3=p2->next;
        p1->next=NULL;
        p2->next=p1;
        while(p3!=NULL){
            p1=p2;
            p2=p3;
            p3=p3->next;
            p2->next=p1;
        }
        head=p2;
    }
};
int main(){
    int n; list a,b,m;
    while(1){
   mm: cout<<"1)List A\n2)List B\n3)Merge\n 4)Exit\nEnter choice: "; cin>>n;
    switch(n){
        case 1:int ch;
        a1: cout<<"1)Add President\n2)Add Secretary\n3)Add Member\n4)Display list\n5)Delete member\n6)Search member\n7)Update member\n8)Reverse list\n9)Previous Menu\n10)Exit\nEnter choice: ";cin>>ch;
        switch(ch){
            case 1: a.insert_at_head(); goto a1;
            case 2: a.insert_at_tail(); goto a1;
            case 3: a.insert_between(); goto a1;
            case 4: a.print(); goto a1;
            case 5: cout<<"Enter position of the member to be deleted"; int x; cin>>x;a.delete_pos(x); goto a1;
            case 6: a.search(); goto a1;
            case 7: a.update(); goto a1;
            case 8: a.reverse(); goto a1;
            case 9: goto mm;
            case 10: goto ex;
            
        } break;
        case 2:int ch1;
        b1: cout<<"1)Add President\n2)Add Secretary\n3)Add Member\n4)Display list\n5)Delete member\n6)Search member\n7)Update member\n8)Reverse list\n9)Previous Menu\n10)Exit\nEnter choice: ";cin>>ch1;
        switch(ch1){
            case 1: b.insert_at_head(); goto b1;
            case 2: b.insert_at_tail(); goto b1;
            case 3: b.insert_between(); goto b1;
            case 4: b.print(); goto b1;
            case 5: cout<<"Enter position of the member to be deleted"; int x; cin>>x;b.delete_pos(x); goto b1;
            case 6: b.search(); goto b1;
            case 7: b.update(); goto b1;
            case 8: b.reverse(); goto b1;
            case 9: goto mm;
            case 10: goto ex;
           
        } break;
        case 3: m.merge(a,b); m.print(); goto mm; break;
        case 4: goto ex; 
    }}
    ex: return 0;
}
