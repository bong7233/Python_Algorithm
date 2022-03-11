# 큰수의법칙

# N개의 숫자를 M번 덧셈하여 나올수있는 최대값( 단, 숫자중 가장 큰 수는 연달아 k번만 더할수 있다)

def bigNum(data,n,m,k):
    data.sort()
    first = data[n-1]  # 가장 큰 수
    sec = data[n-2]    # 그다음 큰 수

    # 가장 큰수가 더해지는 횟수
    # 큰수 k번 반복 + 그다음 큰수1번반복 = 1덩어리 = (K+1)크기를 가짐
    first_count = (m//(k+1)) * k  # 큰덩어리가 더해지는 횟수에 큰덩어리 안에 큰수가 k개 들어있으므로 k 곱해줌
    first_count += (m%(k+1))      # 나눈 나머지만큼 큰수를 더 더해줘야함

    # 그다음 큰수가 더해지는 횟수(총 덧셈횟수인 k에서 큰수를 더하는횟수를 빼면 자연스럽게 그다음큰수의 덧셈횟수나옴)
    sec_count = m-first_count

    # 총합
    total = first_count*first + sec_count*sec
    print(total)

data = [1,4,9,11,20]

bigNum(data,5,10,2)