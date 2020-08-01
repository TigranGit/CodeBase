#include <iostream>
#include <cstdlib>


using namespace std;


struct node {
    int data;
    struct node *next;
} *top;


class stack_list {
    public:
        node *push(node *, int);
        node *pop(node *);
        void traverse(node *);
        stack_list() {
            top = NULL;
        }
};


int main() {
    int choice, item;
    stack_list sl;

    while (1) {
        cout << endl;
        cout << "Select operation:" << endl;
        cout << "1.Push element into the stack" << endl;
        cout << "2.Pop element from the stack" << endl;
        cout << "3.Print the stack" << endl;
        cout << "4.Quit" << endl;
        cout << "Enter your choice: ";

        cin >> choice;
        switch(choice) {
            case 1: {
                cout << "Enter value to be pushed into the stack: ";
                cin >> item;
                top = sl.push(top, item);
                break;
            } case 2: {
                top = sl.pop(top);
                break;
            } case 3: {
                sl.traverse(top);
                break;
            } case 4: {
                exit(0);
                break;
            } default: {
                cout << "Wrong choice!" << endl;
            }
        }
    }

    return 0;
}


node *stack_list::push(node *top, int item) {
    node *tmp;
    tmp = new (struct node);
    tmp->data = item;
    tmp->next = top;
    top = tmp;
    return top;
}


node *stack_list::pop(node *top)
{
    node *tmp;
    if (top == NULL) {
        cout << "Stack is Empty" << endl;
    } else {
        tmp = top;
        cout << "Element Popped: " << tmp->data << endl;
        top = top->next;
        delete(tmp);
    }
    return top;
}


void stack_list::traverse(node *top) {
    node *ptr;
    ptr = top;
    if (top == NULL) {
        cout << "Stack is empty" << endl;
    } else {
        cout << "Stack elements :" << endl;
        while (ptr != NULL) {
            cout << ptr->data << endl;
            ptr = ptr->next;
        }
    }
}
