#include <iostream>


using namespace std;


struct node {
    int data;
    struct node *next;
} *start;


class linked_list {
    public:
        node* create_node(int);
        void insert_begin(int value);
        void insert_pos(int pos, int value);
        void insert_last(int value);
        void delete_pos(int pos);
        void reverse();
        void display();
        linked_list() {
            start = NULL;
        }
};


main() {
    int choice,  i;
    linked_list sl;
    start = NULL;

    while (1) {
        cout << endl;
        cout << "Select operation:" << endl;
        cout << "1.Insert Node at beginning" << endl;
        cout << "2.Insert node at last" << endl;
        cout << "3.Insert node at position" << endl;
        cout << "4.Delete Node" << endl;
        cout << "5.Print Linked List" << endl;
        cout << "6.Reverse Linked List " << endl;
        cout << "7.Exit " << endl;
        cout << "Enter your choice : ";

        cin >> choice;
        switch(choice) {
            case 1: {
                int value;
                cout << "Enter the value to be inserted: ";
                cin >> value;
                sl.insert_begin(value);
                cout << endl;
                break;
            } case 2: {
                int value;
                cout << "Enter the value to be inserted: ";
                cin >> value;
                sl.insert_last(value);
                cout << endl;
                break;
            } case 3: {
                int pos;
                int value;
                cout << "Enter the postion at which node to be inserted: ";
                cin >> pos;
                cout << "Enter the value to be inserted: ";
                cin >> value;
                sl.insert_pos(pos, value);
                cout << endl;
                break;
            } case 4: {
                int pos;
                if (start == NULL) {
                    cout << "List is empty" << endl;
                    break;
                }
                cout << "Enter the postion at which node to be inserted: ";
                cin >> pos;
                sl.delete_pos(pos);
                break;
            } case 5: {
                sl.display();
                cout << endl;
                break;
            } case 6: {
                sl.reverse();
                cout << endl;
                break;
            } case 7 : {
                cout << "Exiting..." << endl;
                exit(0);
                break;
            } default: {
                cout << "Wrong choice" << endl;
            }
        }
    }
}


/*
 * Create a Node
 */
node *linked_list::create_node(int value) {
    struct node *temp, *s;
    temp = new(struct node);
    if (temp == NULL) {
        cout << "Memory not allocated " << endl;
        return 0;
    }
    else {
        temp->data = value;
        temp->next = NULL;
        return temp;
    }
}


/*
 * Insert element at the beginning
 */
void linked_list::insert_begin(int value) {
    struct node *temp, *p;
    temp = create_node(value);
    if (start == NULL) {
        start = temp;
        start->next = NULL;
    }
    else {
        p = start;
        start = temp;
        start->next = p;
    }
    cout << "Element inserted at the beginning" << endl;
}


/*
 * Insert Node at the end
 */
void linked_list::insert_last(int value) {
    struct node *temp, *s;
    temp = create_node(value);
    s = start;
    while (s->next != NULL) {
        s = s->next;
    }
    temp->next = NULL;
    s->next = temp;
}


/*
 * Insert Node at the given position
 */
void linked_list::insert_pos(int pos, int value) {
    int i;
    struct node *temp, *s, *ptr;
    temp = create_node(value);

    if (pos == 1) {
        if (start == NULL) {
            start = temp;
            start->next = NULL;
        } else {
            ptr = start;
            start = temp;
            start->next = ptr;
        }
    } else {
        s = start;
        for (i = 1; i < pos; i++) {
            ptr = s;
            s = s->next;
            if (s == NULL) {
                cout << "Positon out of range" << endl;
                return;
            }
        }
        ptr->next = temp;
        temp->next = s;
    }
}


/*
 * Delete element at the given position
 */
void linked_list::delete_pos(int pos) {
    int i;
    struct node *s, *ptr;
    s = start;
    if (pos == 1) {
        start = s->next;
    }
    else {
        s = start;
        for (i = 1; i < pos; i++) {
            ptr = s;
            s = s->next;
            if (s == NULL) {
                cout << "Positon out of range" << endl;
                return;
            }
        }
        ptr->next = s->next;

        free(s);
        cout << "Element has been deleted" << endl;
    }
}


/*
 * Reverse the Linked List
 */
void linked_list::reverse() {
    struct node *ptr1, *ptr2, *ptr3;
    if (start == NULL) {
        cout << "List is empty" << endl;
        return;
    }
    if (start->next == NULL) {
        return;
    }
    ptr1 = start;
    ptr2 = ptr1->next;
    ptr3 = ptr2->next;
    ptr1->next = NULL;
    ptr2->next = ptr1;
    while (ptr3 != NULL) {
        ptr1 = ptr2;
        ptr2 = ptr3;
        ptr3 = ptr3->next;
        ptr2->next = ptr1;
    }
    start = ptr2;
}


/*
 * Display Elements of the Linked List
 */
void linked_list::display() {
    struct node *temp;
    if (start == NULL) {
        cout << "The List is Empty" << endl;
        return;
    }
    temp = start;
    cout << "Elements of list are: " << endl;
    while (temp != NULL) {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}
