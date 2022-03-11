import collections

# 그룹애너그램 구현
def groupAnagrams(strs: [str]) -> [[str]]:
    # 예외처리를 위한 기본딕셔터리 생성(없는 키값 들어오면 자동으로 키로 설정)
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 단어의 알파벳을 정렬한 후 키값으로 설정하고, 벨류값으로 단어를 넣음
        anagrams[''.join(sorted(word))].append(word)

    # 벨류값들만 리스트로 묶어서 구분
    return list(anagrams.values())

print(groupAnagrams(['abc', 'bac', 'bbb', 'acb']))
# [['abc', 'bac', 'acb'], ['bbb']]