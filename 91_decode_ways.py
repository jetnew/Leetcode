import string
class Solution:
    def __init__(self):
        self.dic = {}
        for i, c in enumerate(string.ascii_uppercase):
            self.dic[str(i+1)] = c
        self.mem = {}
    def numDecodings(self, s: str) -> int:
        if s in self.mem:
            return self.mem[s]
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1 if s in self.dic else 0
        elif n == 2:
            v1 = 1 if s[0] in self.dic and s[1] in self.dic else 0
            v2 = 1 if s[:2] in self.dic else 0
            return v1 + v2
        else:
            v1 = self.numDecodings(s[1:]) if s[0] in self.dic else 0
            v2 = self.numDecodings(s[2:]) if s[:2] in self.dic else 0
            self.mem[s] = v1 + v2
            return self.mem[s]