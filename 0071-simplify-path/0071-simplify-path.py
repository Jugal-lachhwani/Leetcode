class Solution:
    def simplifyPath(self, p: str) -> str:
        if len(p) == 1:
            return p
        if p[len(p) - 1] == '/':
            p = p[0:len(p) -1]
        l = re.findall('[a-z.A-Z_1-9]+',p)
        p = ''
        l1 = []
        i = 0
        while i < len(l):
            if l[i] == '.' or l[i] == '..':
                if l[i] == '..':
                    if i > 0:
                        # print('before pop =',l,i)
                        l.pop(i-1)
                        i = i-1
                        # print('after pop =',l,i)
                l.pop(i)
            else:
                i += 1
        return '/' + '/'.join(l)