class Solution:
    def simplifyPath(self, p: str) -> str:
        if p[len(p) - 1] == '/':
            p = p[0:len(p) -1]
        l = re.findall('[a-z.A-Z_1-9]+',p)
        i = 0
        while i < len(l):
            if l[i] == '.' or l[i] == '..':
                if l[i] == '..':
                    if i > 0:
                        l.pop(i-1)
                        i = i-1
                l.pop(i)
            else:
                i += 1
        return '/' + '/'.join(l)