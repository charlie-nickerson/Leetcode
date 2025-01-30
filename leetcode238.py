# Products of Array Except Self

# Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


def productExceptSelf(nums: list[int]) -> list[int]:
        
        prefix = 1
        products = [1]
        for i in range(len(nums) - 1):
            prefix = nums[i]*prefix
            products.append(prefix)

        postfix = 1
        i = len(nums) - 1
        
        while i >= 0:
            products[i] = products[i]*postfix
            postfix = nums[i]*postfix
            i = i - 1

                

        return products

def main():
    nums = [1,2,4,6]
    product_array = productExceptSelf(nums)
    print(product_array)

if __name__ == "__main__":
    main()