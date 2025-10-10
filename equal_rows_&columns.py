def equalPairs(self, grid):
        n = len(grid)
        row_count = {}

        # Count each row
        for row in grid:
            t = tuple(row)
            row_count[t] = row_count.get(t, 0) + 1

        # Compare with columns
        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in row_count:
                count += row_count[col]

        return count