class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        layers = min(n, m) // 2

        for i in range(layers):
            top = i
            bottom = n - 1 - i
            left = i
            right = m - 1 - i

            arr = []

            # top row
            for c in range(left, right):
                arr.append(grid[top][c])

            # right column
            for r in range(top, bottom):
                arr.append(grid[r][right])

            # bottom row
            for c in range(right, left, -1):
                arr.append(grid[bottom][c])

            # left column
            for r in range(bottom, top, -1):
                arr.append(grid[r][left])

            l = len(arr)
            rot = k % l

            # anti-clockwise rotation
            rt_arr = arr[rot:] + arr[:rot]

            idx = 0

            for c in range(left, right):
                grid[top][c] = rt_arr[idx]
                idx += 1

            for r in range(top, bottom):
                grid[r][right] = rt_arr[idx]
                idx += 1

            for c in range(right, left, -1):
                grid[bottom][c] = rt_arr[idx]
                idx += 1

            for r in range(bottom, top, -1):
                grid[r][left] = rt_arr[idx]
                idx += 1

        return grid