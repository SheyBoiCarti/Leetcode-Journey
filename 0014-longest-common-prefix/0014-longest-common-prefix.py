class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        possiblePrefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(possiblePrefix):
                possiblePrefix = possiblePrefix[:-1]

                if len(possiblePrefix) == 0:
                    return ""

        return possiblePrefix