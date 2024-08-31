nums = [2,4,7,15]
target = 9

for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"Target located ({i},{j})")