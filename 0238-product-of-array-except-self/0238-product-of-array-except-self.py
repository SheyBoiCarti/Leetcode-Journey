class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        Prefix_left_product = [0] * len(nums)
        Suffix_right_Product = [0] * len(nums)

        Prefix_left_product[0] = nums[0]
        Suffix_right_Product[len(nums) - 1] = nums[len(nums) - 1]

        # The idea is to get the product of everything to the left
        # and everything to the right of the current number
        # Then multiply those together so the current number is excluded

        result = [0] * len(nums)

        # Build up the products from left to right
        for i in range(1, len(nums)):
            Prefix_left_product[i] = Prefix_left_product[i - 1] * nums[i]

        # Build up the products from right to left
        for j in range(len(nums) - 2, -1, -1):
            Suffix_right_Product[j] = Suffix_right_Product[j + 1] * nums[j]

        for i in range(len(nums)):

            if i == 0:
                # First number has nothing to the left
                # so we only need the product of everything to the right
                result[i] = Suffix_right_Product[i + 1]

            elif i == len(nums) - 1:
                # Last number has nothing to the right
                # so we only need the product of everything to the left
                result[i] = Prefix_left_product[i - 1]

            else:
                # Multiply everything to the left by everything to the right
                result[i] = Prefix_left_product[i - 1] * Suffix_right_Product[i + 1]

        return result