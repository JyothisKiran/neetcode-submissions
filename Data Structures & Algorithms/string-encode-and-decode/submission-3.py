class Solution:

    def encode(self, strs: List[str]) -> str:
        _strs = []
        for s in strs:
            _strs.append(str(len(s)).zfill(4))
            _strs.append("#")
            _strs.append(s)
        return ''.join(_strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        pointer = 0
        while (pointer < len(s)):
            length = int(s[pointer : pointer+4])
            pointer+=4
            if(s[pointer]=="#"):
                pointer+=1
                strs.append(s[pointer : pointer+length])
                pointer+=length
        return strs
