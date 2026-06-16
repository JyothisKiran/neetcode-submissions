class Solution:

    def encode(self, strs: str) -> str:
        _strs = []
        for st in strs:
                _strs.append(str(len(st)).zfill(4))
                _strs.append('#')
                _strs.append(st)
        return ''.join(_strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        pointer = 0

        while (pointer < len(s)):
                print(pointer)
                length = int(s[pointer : pointer+4])
                pointer += 4
                if (s[pointer] == '#'):
                    pointer+= 1 # skipping #
                    strs.append(s[pointer : pointer+length])
                    pointer += length
        return strs 