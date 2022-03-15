###
'''
리스트에서 pop(1)메서드를 사용하면
맨앞의 값을 뽑앗을때 나머지요소를 모두 한칸씩 앞으로 당겨야하므로 O(n)의 시간복잡도를 가지지만
Deque에서 popleft()을 사용하면 O(1)의 시간복잡도를 가진다
이것을 활용하여 주어진 연결리스트를 Deque로 변환하여 풀이하는 방법도 있다
추가로 Runner(투포인터와 비슷한 방식)을 이용한 풀이법도 고민해봐야한다
'''
###

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


# 테스트
def isPalindromeList(head:ListNode) -> bool:
    arr = []

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) >1:
        if arr.pop(0) != arr.pop():
            return False

    return True

## 연결리스트 생성
li = LinkedList()
for i in [1,3,3,1]:
    li.append(i)

li2 = LinkedList()
for i in [1,5,1,1]:
    li2.append(i)


assert isPalindromeList(li.head)
assert not isPalindromeList(li2.head)
