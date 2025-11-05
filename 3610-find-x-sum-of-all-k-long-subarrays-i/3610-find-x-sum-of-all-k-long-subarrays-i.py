class Solution:
    def findXSum(self, n: List[int], k: int, x: int) -> List[int]:
        answer = []
        nums = len(n)
        d = {}
        for o in range(nums-k+1):
            if not d:
                for r in range(o,k+o):
                    if n[r] in d:
                        d[n[r]] += 1
                    else:
                        d[n[r]] = 1
            else:
                d[n[o-1]] -= 1
                if n[k+o-1] in d:
                    d[n[k+o-1]] += 1
                else:
                    d[n[k+o-1]] = 1
            l = list(d.items())
            sum = 0
            for i in range(x):
                if i >= len(l):
                    break
                m = i
                for j in range(i+1,len(l)):
                    c = j
                    if l[c][1] > l[m][1]:
                        m = c
                    elif l[c][1] == l[m][1]:
                        if l[c][0] > l[m][0]:
                            m = c
                sum += l[m][0] * l[m][1]
                (l[i],l[m]) = (l[m],l[i])
            answer.append(sum)  
        return answer