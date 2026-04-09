from collections import deque

# ── Grid size ──
GRID_SIZE = 11  # positions 0 to 10

def create_grid():
    # All cells start as safe (1)
    # grid[row][col] — row 0 is north, row 10 is south
    return [[1] * GRID_SIZE for _ in range(GRID_SIZE)]


def mark_obstacles(grid, file_path):
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Parse the 4 values
            values = list(map(int, line.split()))
            north, east, south, west = values

            # The obstacle occupies a rectangular region
            # North and South define the row range
            # East and West define the column range
            # Row increases going south, decreases going north
            row_start = north
            row_end   = south if south != 0 else north
            col_start = west
            col_end   = east

            # Mark all cells in this rectangle as obstacle (0)
            for row in range(min(row_start, row_end),
                             max(row_start, row_end) + 1):
                for col in range(min(col_start, col_end),
                                 max(col_start, col_end) + 1):
                    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                        grid[row][col] = 0


def print_grid(grid, path=None):
    # Convert path to a set for O(1) lookup
    path_cells = set(path) if path else set()

    print("\n── Arena Map ──")
    print("  " + " ".join(str(c) for c in range(GRID_SIZE)))

    for row in range(GRID_SIZE):
        row_str = str(row) + " "
        for col in range(GRID_SIZE):
            if (row, col) == (0, 0):
                row_str += "S "    # Start
            elif (row, col) == (10, 10):
                row_str += "E "    # End
            elif (row, col) in path_cells:
                row_str += "* "    # Path
            elif grid[row][col] == 0:
                row_str += "X "    # Obstacle
            else:
                row_str += ". "    # Safe
        print(row_str)

    print("\nLegend: S=Start  E=End  *=Path  X=Obstacle  .=Safe")


def bfs(grid, start, end):
    # BFS — explore level by level
    # Queue stores (current_position, path_so_far)
    queue = deque()
    queue.append((start, [start]))

    # Visited set — don't revisit cells
    visited = set()
    visited.add(start)

    # Four possible moves — up, down, left, right
    # (no diagonal movement as per task)
    moves = [(-1, 0),   # North
             ( 1, 0),   # South
             ( 0, 1),   # East
             ( 0, -1)]  # West

    while queue:
        # Take the next cell to explore
        (row, col), path = queue.popleft()

        # Check if we reached the destination
        if (row, col) == end:
            return path

        # Try all 4 directions
        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc
            new_pos = (new_row, new_col)

            # Check bounds
            if not (0 <= new_row < GRID_SIZE and
                    0 <= new_col < GRID_SIZE):
                continue

            # Check not visited
            if new_pos in visited:
                continue

            # Check not an obstacle
            if grid[new_row][new_col] == 0:
                continue

            # Valid move — add to queue
            visited.add(new_pos)
            queue.append((new_pos, path + [new_pos]))

    # If queue empties without finding end — no path exists
    return None


if __name__ == "__main__":
    file_path = input("Enter obstacle file path: ").strip()

    # Step 1 — Build grid
    grid = create_grid()

    # Step 2 — Mark obstacles
    mark_obstacles(grid, file_path)

    # Step 3 — Print grid without path
    print_grid(grid)

    # Step 4 — Find shortest path
    start = (0, 0)
    end   = (10, 10)

    print("\nFinding shortest path from [0,0] to [10,10]...")
    path = bfs(grid, start, end)

    # Step 5 — Print result
    if path:
        print(f"Shortest path found! Length: {len(path)} steps")
        print(f"Path: {path}")
        print_grid(grid, path)
    else:
        print("No path exists — destination unreachable!")