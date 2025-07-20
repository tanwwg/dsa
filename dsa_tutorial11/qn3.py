class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def count(l):
    if l is None: return 0
    return 1 + count(l.next)

print(count(list1))
