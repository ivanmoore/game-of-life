import random
import time


class Rules(object):
    def shouldCellStayAlive(self, numberOfNeighbours):
        return numberOfNeighbours in [2, 3]

    def shouldCellSpringIntoLife(self, numberOfNeighbours):
        return numberOfNeighbours == 3


class Grid(object):
    def __init__(self):
        self.cells = set()

    def isLiveCellAt(self, x, y):
        return (x, y) in self.cells

    def addCellAt(self, x, y):
        self.cells.add((x, y))

    def numberOfNeighbours(self, x, y):
        offsets = [(xOffset, yOffset) for xOffset in [-1, 0, 1] for yOffset in [-1, 0, 1] if
                   not (xOffset == 0 and yOffset == 0)]
        neighbours = 0
        for offset in offsets:
            if self.isLiveCellAt(x + offset[0], y + offset[1]):
                neighbours += 1
        return neighbours

    def nextGeneration(self):
        newGrid = Grid()
        for cell in self.cells:
            if Rules().shouldCellStayAlive(self.numberOfNeighbours(cell[0], cell[1])):
                newGrid.addCellAt(cell[0], cell[1])
        minX, minY, maxX, maxY = self.bounds()
        for x in range(minX - 1, maxX + 2):
            for y in range(minY - 1, maxY + 2):
                if Rules().shouldCellSpringIntoLife(self.numberOfNeighbours(x, y)):
                    newGrid.addCellAt(x, y)
        return newGrid

    def bounds(self):
        if len(self.cells) == 0:
            return (0, 0, 0, 0)
        xValues = [c[0] for c in self.cells]
        minX = min(xValues)
        maxX = max(xValues)
        yValues = [c[1] for c in self.cells]
        minY = min(yValues)
        maxY = max(yValues)
        return (minX, minY, maxX, maxY)

    def toString(self, boundsToDisplay):
        minX, minY, maxX, maxY = boundsToDisplay
        result = ""
        for y in range(maxY, minY - 1, -1):
            for x in range(minX, maxX + 1):
                if self.isLiveCellAt(x, y):
                    result += "x"
                else:
                    result += "-"
            result += "\n"
        return result


if __name__ == "__main__":
    grid = Grid()
    for i in range(0, 20):
        grid.addCellAt(random.randint(0, 20), random.randint(0, 10))
    x0, y0, x1, y1 = grid.bounds()
    outerBounds = (x0 - 1, y0 - 1, x1 + 1, y1 + 1)
    for i in range(1, 20):
        print(grid.toString(outerBounds))
        grid = grid.nextGeneration()
        time.sleep(1)