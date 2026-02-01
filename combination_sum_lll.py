def combinationSum3(self, k, n):
        res = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return

            for num in range(start, 10):
                if total + num > n:
                    break

                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()

        backtrack(1, [], 0)
        return res
