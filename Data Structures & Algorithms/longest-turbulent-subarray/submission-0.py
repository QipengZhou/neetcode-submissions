class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dec = 1
        inc = 1
        max_len = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            else:
                dec = 1
                inc = 1
            max_len = max(max_len, inc, dec)
        return max_len
        