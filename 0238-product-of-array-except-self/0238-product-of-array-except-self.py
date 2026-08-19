class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        Prefix_left_product = [0] * len(nums)
        Suffix_right_Product = [0] * len(nums)
        result = [0] * len(nums)

        Prefix_left_product[0] = 1
        Suffix_right_Product[len(nums) - 1] = 1

        
        for i in range(1, len(nums)):
            Prefix_left_product[i] = Prefix_left_product[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            Suffix_right_Product[j] = Suffix_right_Product[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            result[i] = Prefix_left_product[i] * Suffix_right_Product[i]

        return result