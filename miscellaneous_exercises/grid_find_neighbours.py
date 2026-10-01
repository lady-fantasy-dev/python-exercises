# Find right and bottom neighbors in grid

grid = [
    "0..0.",
    "..0..",
    "....0",
    "0...."
]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      if cell == "0":
        node = [x, y]

        # find right neighbour
        for right_x in range(x + 1, len(row)):
            if row[right_x] == "0":
              right_neighbour = [right_x, y]
              break
        else:
            right_neighbour = [-1, -1]

        # find bottom neighbour
        for bottom_y in range(y+1, len(grid)):
            if grid[bottom_y][x] == "0" :
              bottom_neighbour = [x, bottom_y]
              break

        else:
            bottom_neighbour = [-1, -1]

        print(node, right_neighbour, bottom_neighbour)
