class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isfeasible(speed: int) -> bool:
            return sum(math.ceil(pile/speed) for pile in piles) <= h
        l, r = 1, max(piles)
        while l <= r:
            rate = l + (r-l)//2
            if isfeasible(rate):
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        return res




            