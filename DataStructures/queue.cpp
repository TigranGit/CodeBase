#include <iostream>
#include <cstdlib>

#define QUEUE_SIZE 10

using namespace std;


class queue {
    int arr[QUEUE_SIZE];
    int head;
    int tail;
    int count;

    public:
        queue() {
            head = -1;
            tail = -1;
            count = 0;
        }

        int dequeue();
        void enqueue(int item);
        int size();
        void display();
};


int main() {
    int choice;
    queue my_queue;

    while (1) {
        cout << endl;
        cout << "Select operation:" << endl;
        cout << "1.Enqueue" << endl;
        cout << "2.Dequeue" << endl;
        cout << "3.Print the Queue" << endl;
        cout << "4.Print the size of Queue" << endl;
        cout << "5.Exit " << endl;
        cout << "Enter your choice : ";

        cin >> choice;
        switch(choice) {
            case 1: {
                int value;
                cout << "Enter the value to be inserted: ";
                cin >> value;
                my_queue.enqueue(value);
                cout << endl;
                break;
            } case 2: {
                cout << "The element is " << my_queue.dequeue() << endl;
                break;
            } case 3: {
                my_queue.display();
                break;
            } case 4: {
                cout << "The size of Queue is " << my_queue.size() << endl;
                break;
            } case 5: {
                cout << "Exiting..." << endl;
                exit(0);
                break;
            } default: {
                cout << "Wrong choice" << endl;
            }
        }
    }
    return 0;
}


/**
 * Add an item to the queue
*/
void queue::enqueue(int item) {
    if (head == -1) {
        head++;
    }
    if (tail == QUEUE_SIZE - 1) {
        cout << "Queue is full";
    } else {
	    tail = (tail + 1) % QUEUE_SIZE; // For circulation
        arr[tail] = item;
    }
}

/**
 * Pop head element from the queue
 * Return NULL if the queue is empty
*/
int queue::dequeue() {
    int item;

    if (count == QUEUE_SIZE) {
        cout << "The queue is empty!" << endl;
        return -1;
    }

    item = arr[head];
    head = (head + 1) % QUEUE_SIZE; // For circulation
    return item;
}

/**
 * Display the queue elements
*/
void queue::display() {
    for (int i = head; i <= tail; ++i) {
        cout << arr[i] << endl;
    }
}

/**
 * Return the size of the queue
*/
int queue::size() {
    return count;
}
