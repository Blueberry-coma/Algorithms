#88095796
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else: 
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return - 1



def main():
    print(broken_search(nums, target))

if __name__ == '__main__':
    main()