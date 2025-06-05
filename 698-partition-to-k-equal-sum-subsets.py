def solution(nums: list[int], k: int) -> bool:
     target = sum(nums)
     if target % k != 0:
         return False
     target //= k

     res = False

     def backtrack(i, curr_sums):
         nonlocal res

         if i == len(nums):
             if not res:
                 print(curr_sums)
             res = True
             return

         for j in range(k):
             if nums[i] <= target - curr_sums[j]:
                curr_sums[j] += nums[i]
                backtrack(i + 1, curr_sums)
                curr_sums[j] -= nums[i]

     curr_sums = [0] * k
     backtrack(0, curr_sums)

     return res

print(solution([2,2,2,2,3,4,5], 4))
