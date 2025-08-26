class Solution:
    def threeSumClosest(self, l: List[int], target: int) -> int:
        l.sort()
        n = len(l)

        diff = float("inf")
        
        for i in range(len(l)):

            j = i + 1
            k = len(l) - 1

            requiredSum = target - l[i]

            while j < k:

                if l[j] + l[k] == requiredSum:
                    return target
                if diff > abs(requiredSum - l[j] - l[k]):
                    diff = abs(requiredSum - l[j] - l[k])
                    closestSum = l[i] + l[j] + l[k]
                elif l[j] + l[k] > requiredSum:
                    k = k - 1
                else:
                    j = j + 1
        return closestSum  