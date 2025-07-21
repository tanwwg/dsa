class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def findSecondLast(node, prev=None):
    if node is None or node.next is None: return prev
    return findSecondLast(node.next, node)

print(findSecondLast(head).val)


