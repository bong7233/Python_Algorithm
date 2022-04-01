from collections import defaultdict
import re

def solution(files):

    if len(files) == 0:
        return []
    head = re.compile('[a-zA-Z]+')
    number = re.compile('[0-9]{1,5}')

    file_dic = defaultdict(list)

    for file in files:
        file_head = head.search(file).group()
        file_num = number.search(file).group()

        file_dic[file].append(file_head.lower())
        file_dic[file].append(int(file_num))

    file_sorted = sorted(file_dic.items(), key=lambda x : (x[1][0], x[1][1]))
    print(file_sorted)
    answer = []
    for file in file_sorted:
        answer.append(file[0])

    print(answer)

li = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

solution(li)


s= "img12asg.png"

t = re.split(r"([0-9]+)",s)
print(t)