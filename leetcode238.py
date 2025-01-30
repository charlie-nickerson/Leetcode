# Products of Array Except Self

# Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


def productExceptSelf(nums: list[int]) -> list[int]:
    
    product, num_zeros, product_array = 1, 0, []
    
    # Calculate the product of the array without zeros and count the amount of zeros that are present
    for n in nums:
        if n == 0: num_zeros += 1
        else: product = n*product

    # If the array contains more than 2 zeros then the product of every element of the array is zero
    if num_zeros > 1:  return [0] * len(nums)

    else:
        for n in nums:
            
            # If there exists one zero in the array make sure to set the element of the array to the product of the array without the zeros
            if num_zeros > 0:
                
                if n == 0: product_array.append(product)
                
                # All other non zeros elements have a product of zero
                else: product_array.append(0)
            
            # If there arent any zeros present just take the product of the array and divide it by the current element
            else: product_array.append(int(product/n))
    return product_array

def main():
    nums = [1,2,4,6]
    product_array = productExceptSelf(nums)
    print(product_array)

if __name__ == "__main__":
    main()