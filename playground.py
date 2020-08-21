
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    val = 0
    for num in nums:
        print(f'before xor {bin(val)} \n')
        val ^= num
        print(f'after xor {bin(val)} \n')
    return val


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    singleNumber(nums)
