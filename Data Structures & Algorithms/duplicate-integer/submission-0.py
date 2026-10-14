class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table={}
        for num in nums:
            hash_table[num]=hash_table.get(num,0)+1
        for x in hash_table.values():
            if x>1:
                return True
        return False
