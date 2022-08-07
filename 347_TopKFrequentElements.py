#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        maxHeap = [(-v, k)for k,v in count.items()]
        heapq.heapify(maxHeap)
        
        res = []
        while k > 0:
            v, a = heapq.heappop(maxHeap)
            k-=1
            res.append(a)
        return res
