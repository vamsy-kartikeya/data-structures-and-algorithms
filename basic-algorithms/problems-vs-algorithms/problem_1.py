"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    low, high = 0 , number
    ans = 0
    while low <= high :
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number : 
            ans = mid
            low = mid + 1  
        else :
            high = mid - 1
    return ans

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
