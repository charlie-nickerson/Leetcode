# Top K Frequent Elements

# Description: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    c = Counter(nums)
    top_k = []
    freq = [[] for _ in range(len(nums) + 1)]
    for key in c.keys():
        freq[c[key]].append(key)
    for f in reversed(freq):
        while f and k:
            top_k.append(f.pop())
            k = k - 1
    return top_k

def main():
    nums = [1,2,2,3,3,3]
    k = 2
    top_k = topKFrequent(nums, k)
    print(top_k)

if __name__ == "__main__":
    main()