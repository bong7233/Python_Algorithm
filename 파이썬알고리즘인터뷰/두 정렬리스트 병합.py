
## 추가적인 이해가 필요하다
## 재귀를 사용하는것이 핵심이지만, li1 과 li2의 치환과정이 정훡하게 이해되지않음...

from linkedList import LinkedList, ListNode

def mergeTwoLists(li1: [ListNode], li2: [ListNode]) -> [ListNode]:
    if (not li1) or (li2 and li1.val > li2.val):
        li1, li2 = li2, li1
    if li1:
        li1.next = mergeTwoLists(li1.next, li2)
    return li1


###### 내가 이해한 풀이법 ######

def mergeTwoLists(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    # 결과를 담을 비어있는 노드생성
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            # l2가 더 클때 tail이 l1을 가리키게하고 l1은 한칸넘어간다
            tail.next = l1
            l1 = l1.next
        else:
            # l1이 더 크다면 tail이 l2를 가리키게 하고 l2는 한칸넘어간다
            tail.next = l2
            l2 = l2.next
        tail = tail.next   # 과정이 끝나면 tail도 가리키던곳으로 이동한다

    # 여기부터는 l1,l2중 하나의 더 길때 남은부분을 tail뒤에 덩어리로 다 붙이는 과정이다
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    # 과정이 끝나면 tail을따라 정렬된 리스트가 완성된다 [1,1,2,3...]
    # tail은 처음 dummy에서 시작하였으므로 dummy.next를하면 tail이 왔던길을따라서
    # 정렬된리스트가 쭉 출력된다
    return dummy.next

# 시간복잡도는 O(l1의길이 + l2의 길이)
# 공간복잡도는 O(1)
