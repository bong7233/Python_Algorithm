# 연결리스트를 뒤집기위해 재귀를 사용할수있다
from linkedList import ListNode

def reverseList(head: [ListNode]) -> [ListNode]:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)



## 반복구조로 뒤집을수도있다
# Time : O(n)
# space: O(1)

def reverseList(head: [ListNode]) -> [ListNode]:
    # head를 가리키는 curr 포인터, 비어있는공간을 가리키는 prev 포인터를 만든다
    # 쉽게 이해하기위해 원래의 리스트 왼쪽에 비어있는 prev 노드를 만든다고 생각하면된다
    curr, prev = head, None

    # curr 포인터가 None을 가리킬떄까지 반복(즉 리스트 끝까지 반복)
    while curr:
        next = curr.next  # 우선 현제 curr 포인터의 다음을 가리키는 next 포인터를 생성
        curr.next = prev  # 그다음 curr포인터가 있는(head)의 화살표방향을 반대로바꿈
        prev = curr       # prev 포인터를 curr 위치로 이동시킨다
        curr = next       # curr 포인터를 next 위치로 이동시킨다

    # 반복이 끝나면 prev포인터는 리스트의 마지막노드를 가리키고있음
    # curr,next 포인터는 리스트밖으로 나가게된다(None)
    # prev포인터(마지막노드)를 호출하면 바꿔두엇던 화살표방향대로 쭉 역순호출된다
    return prev

