class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toList(l):
    if l is None: return []
    return [l.val] + toList(l.next)

def find(l, x, prev=None):
    if l is None: return None, None
    if l.val == x: return prev, l
    return find(l.next, x, l)

class HeadTailList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, x):
        if self.head is None:
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def remove(self, x):
        prev, rem = find(self.head, x)
        if rem is None:
            pass
        elif rem == self.head:
            self.head = self.head.next
            if self.head is None: self.tail = None
        elif rem == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = rem.next

    def toList(self):
        return toList(self.head)

ht = HeadTailList()
ht.append(1)
ht.append(2)
ht.append(3)
ht.append(4)
assert ht.toList() == [1, 2, 3, 4]

ht = HeadTailList()
ht.append(1)
ht.remove(1)
assert ht.toList() == []
ht.append(1)
ht.append(2)
ht.remove(2)
assert ht.toList() == [1]
ht.append(3)
assert ht.toList() == [1, 3]

