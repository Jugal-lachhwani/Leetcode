class Solution:
    def findXSum(self, n: List[int], k: int, x: int) -> List[int]:
        answer = []
        nums = len(n)
        for o in range(nums-k+1):
            d = {}
            for r in range(o,k+o):
                if n[r] in d:
                    d[n[r]] += 1
                else:
                    d[n[r]] = 1
            l = list(d.items())
            sum = 0
            # print(l)
            for i in range(x):
                # print('i=',i)
                # print('x=',x)
                if i >= len(l):
                    break
                m = i
                # print('l[m]',l[m])
                for j in range(i+1,len(l)):
                    print('j',j)
                    c = j
                    # print('l[c]',l[c])
                    # print('l[m]',l[m])
                    if l[c][1] > l[m][1]:
                        m = c
                    elif l[c][1] == l[m][1]:
                        if l[c][0] > l[m][0]:
                            m = c
                # print('l[m]',l[m])
                sum += l[m][0] * l[m][1]
                (l[i],l[m]) = (l[m],l[i])
            answer.append(sum)  
        # d = sorted(d.items(),key = lambda x:(x[1],x[0]),reverse = True)
        # print(l)
        # print(d)
        return answer