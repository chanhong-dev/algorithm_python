import sys



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        self.tail.next = new
        self.tail = new
        return

    def pop(self):
        if self.head is None:
            return '-1'
        delete = self.head
        self.head = self.head.next
        return delete.data

    def size(self):
        cnt = 0
        cur = self.head
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def empty(self):
        answer = 0
        if self.head is None:
            answer = 1
        return answer

    def front(self):
        if self.head is None:
            return '-1'
        return self.head.data

    def back(self):
        if self.head is None:
            return '-1'
        return self.tail.data


queue = Queue()
num = int(sys.stdin.readline())
for i in range(num):
    order = sys.stdin.readline().strip().split()

    command = order[0]

    if command == 'push':
        queue.push(order[1])
    elif command == 'pop':
        print(queue.pop())
    elif command == 'size':
        print(queue.size())
    elif command == 'empty':
        print(queue.empty())
    elif command == 'front':
        print(queue.front())
    else:
        print(queue.back())
