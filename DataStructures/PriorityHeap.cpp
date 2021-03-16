/* Compile command: g++ -o PriorityHeap.exe -std=c++11 -static-libgcc -static-libstdc++ .\PriorityHeap.cpp */

#define PARENT(i) (i - 1) / 2
#define LEFT(i) (2 * i) + 1
#define RIGHT(i) (2 * i) + 2
#define INF 1e9

#include "iostream"

using namespace std;

class PQueue {
    int n, *data, length;

public:
    PQueue();
    void init(int);
    void max_heapify(int);
    void build_max_heap();
    void display();
    int get_maximum();
    int extract_max();
    void increase_key(int, int);
    void insert(int);
    ~PQueue();
};

PQueue::PQueue() {
    length = 0;
    data = NULL;
}

void PQueue::init(int size) {
    // initialize the array
    length = size - 1;
    data = new int[2 * size];
}

void PQueue::max_heapify(int i) {
    // heapify function
    int l = LEFT(i);
    int r = RIGHT(i);
    int largest = i;

    if (LEFT(i) <= length && data[l] > data[largest]) {
        largest = l;
    }
    if (RIGHT(i) <= length && data[r] > data[largest]) {
        largest = r;
    }

    if (largest != i) {
        int temp = data[i];
        data[i] = data[largest];
        data[largest] = temp;
        max_heapify(largest);
    }
}

void PQueue::build_max_heap() {
    // print queue elements
    for (int i = PARENT(length); i >= 0; i--) {
        max_heapify(i);
    }
}

void PQueue::display() {
    // print queue elements
    if (length < 1) {
        cout << "no elements" << endl;
    } else {
        cout << "elements are:" << endl;
        for (int i = 0; i < length; i++) {
            cout << data[i] << endl;
        }
    }
}

int PQueue::get_maximum() {
    // get the max key
    return data[0];
}

int PQueue::extract_max() {
    // extract the max key, will be removed
    int m = data[0];
    data[0] = data[length];
    length--;
    max_heapify(0);
    return m;
}

void PQueue::increase_key(int i, int key) {
    // increase key's value by pos
    if (data[i] > key) {
        cout << "error: new key is smaller than current key" << endl;
    } else {
        data[i] = key;
        while (data[PARENT(i)] < data[i] && i > 0) {
            int temp = data[PARENT(i)];
            data[PARENT(i)] = data[i];
            data[i] = temp;
            i = PARENT(i);
        }
    }
}

void PQueue::insert(int key) {
    // insert new key
    length++;
    data[length] = -INF;
    increase_key(length, key);
}

PQueue::~PQueue()
{
    delete[] data;
}

int main() {
	PQueue pqueue;
    int max;

	pqueue.init(0);
	pqueue.display();

    pqueue.insert(1);
    pqueue.insert(3);
    pqueue.insert(2);
    pqueue.insert(10);
    pqueue.increase_key(2, 5);

	pqueue.build_max_heap();
	pqueue.display();

    cout << "maximum element is " << pqueue.get_maximum() << endl;
    max = pqueue.extract_max();
    cout << "extracted maximum element is " << max << endl;
    cout << "maximum element is " << pqueue.get_maximum() << endl;

    return 0;
}
