class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        arr = sorted(count.values())
        arr = arr[len(arr) - k:]

        res = []
        for i, v in count.items():
            if v in arr:
                res.append(i)
        print(res)
        return res