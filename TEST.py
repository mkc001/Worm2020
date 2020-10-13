def permute(nums):
    size = len(nums)
    if size == 0:
        return []
    nums.sort()

    res = []

    def dfs(first = 0):
        if first == size:
            res.append(nums[:])
        for i in range(first,size):
            nums[first],nums[i] = nums[i],nums[first]
            dfs(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    dfs()
    print(res)
    return res



permute([1,2,3])