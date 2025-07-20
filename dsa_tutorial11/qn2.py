class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list2 = ListNode(5, ListNode(6, ListNode(7, ListNode(8))))

def findLast(l):
    if l.next == None: return l
    return findLast(l.next)

def concat(l, m):
    findLast(l).next = m

def toList(l):
    if l is None: return []
    return [l.val] + toList(l.next)

concat(list1, list2)
print(toList(list1))

