from linkedList import ListNode

def oddEvenList(self, head: [ListNode]) -> [ListNode]:
    # 예외처리
    if head is None:
        return None

    # 홀수포인터를 head에 짝수포인터를 even에두고
    # 후에 odd의 끝을 even의 처음에 연결하기위해 even_head도 미리 설정한다
    odd = head
    even = head.next
    even_head = head.next

    # 반복문의 조건이 odd가 아니라 even인 이유에대해 생각해보자
    while even and even.next:
        # 먼저 next를 찍어두고나서 , 포인터가 따라가는 방식으로했기떄문에
        # 새로운 공간을 생성하지않아 space : O(1)이 가능하다
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head

    return head

