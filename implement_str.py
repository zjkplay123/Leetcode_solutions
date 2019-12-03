
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return (0)
        elif needle not in haystack:
            return (-1)
        else:
            if haystack==needle:
                return (0)
            else:
                n=len(needle)
                for i in range(len(haystack)-n+1):
                    if haystack[i:i+n]==needle:
                        return i