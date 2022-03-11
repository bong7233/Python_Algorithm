def threeSum(nums:[int]) -> [[int]]:
    result = [] # 빈리스트생성
    nums.sort() # 들어온 리스트 정렬

    for i in range(len(nums) -2):
        # 값이 중복되는경우 생략
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 투포인터 생성
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # 세수의 합이 0이 되고나서 각 포인터의 중복값을 생략
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 중복값 건너뛴 후 양 포인터를 한칸씩 더 움직여서 다시 left<right while문 실행
                left += 1
                right -= 1

    return result

print(threeSum([1, 2, 4, 5, -1, -4, -3, -2]))
# [[-4, -1, 5], [-3, -2, 5], [-3, -1, 4], [-3, 1, 2]]