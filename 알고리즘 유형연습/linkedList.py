# 리스트노드
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 연결리스트 구조
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)



