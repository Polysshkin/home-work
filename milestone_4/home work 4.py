import time # Get the current time to measure execution duration
from typing import List, Tuple
from collections import Counter
import re

start = time.time()

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    
    #Brute force approach: Iterate through all possible pairs.
    #Time complexity: O(n^2) - due to the nested loop.
    #Space complexity: O(1) - no additional space used.
   
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return i, j  # Return the first found pair
    return -1, -1  # This case will never be reached as per problem constraints

def word_frequency(text: str):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def are_anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


print(find_sum(5, [1, 2, 3, 4, 5]))
assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

text = "This is a sample text. This text is a good example."
print("\nWord frequency result:", word_frequency(text))


str1 = "listen"
str2 = "silent"
print("\nAnagram check result:", are_anagrams(str1, str2))  # Output: True


end = time.time()

print(f"Execution time: {end - start} seconds")
 ###############################################################

import time
from typing import List, Tuple
from collections import Counter
import re

start = time.time()

# Function to find the sum
def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    # Optimized approach: using a hash table for faster lookup.
    # Time complexity: O(n) - a single pass through the list.
    # Space complexity: O(n) - additional memory used for storing numbers.
    
    seen = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(li):
        complement = target - num  # Calculate the required complement
        if complement in seen:
            return seen[complement], i  # Return indices if complement found
        seen[num] = i  # Store the number with its index
    return -1, -1  # This case will never be reached as per problem constraints

# Function to count word frequency
def word_frequency(text: str):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

# Function to check if two strings are anagrams
def are_anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

# Test the find_sum_fast function
print("Find sum result:", find_sum_fast(5, [1, 2, 3, 4, 5]))

# Assert the correctness of the function
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

# Example text for the word frequency function
text = "This is a sample text. This text is a good example."

# Print the result of the word frequency function
print("\nWord frequency result:", word_frequency(text))

# Test the anagram check function
str1 = "listen"
str2 = "silent"
print("\nAnagram check result:", are_anagrams(str1, str2))  # Output: True

end = time.time()

# Print the execution time
print(f"\nExecution time: {end - start} seconds")