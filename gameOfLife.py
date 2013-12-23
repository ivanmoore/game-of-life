import random
import time


class Rules(object):
    def shouldCellStayAlive(self, numberOfNeighbours):
        return numberOfNeighbours in [2, 3]

    def shouldCellSpringIntoLife(self, numberOfNeighbours):
        return numberOfNeighbours == 3

class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.x) + hash(self.y)

class Grid(object):
    def __init__(self):
        self.cells = set()

    def isLiveCellAt(self, x, y):
        return Cell(x, y) in self.cells

    def addCellAt(self, x, y):
        self.cells.add(Cell(x, y))

    def numberOfNeighbours(self, x, y):
        offsets = [Cell(xOffset, yOffset) for xOffset in [-1, 0, 1] for yOffset in [-1, 0, 1] if
                   not (xOffset == 0 and yOffset == 0)]
        neighbours = 0
        for offset in offsets:
            if self.isLiveCellAt(x + offset.x, y + offset.y):
                neighbours += 1
        return neighbours
        
    def getNeighboursOfCell(self, x, y):
        offsets = [Cell(xOffset, yOffset) for xOffset in [-1, 0, 1] for yOffset in [-1, 0, 1]]
        neighbours = set()
        for offset in offsets:
            neighbours.add(Cell(x + offset.x, y + offset.y))
        return neighbours

    def nextGeneration(self):
        newGrid = Grid()
        for cell in self.cells:
            if Rules().shouldCellStayAlive(self.numberOfNeighbours(cell.x, cell.y)):
                newGrid.addCellAt(cell.x, cell.y)
            for neighbour in self.getNeighboursOfCell(cell.x, cell.y):
                if Rules().shouldCellSpringIntoLife(self.numberOfNeighbours(neighbour.x, neighbour.y)):
                    newGrid.addCellAt(neighbour.x, neighbour.y)
        return newGrid

    def bounds(self):
        if len(self.cells) == 0:
            return (0, 0, 0, 0)
        xValues = [c.x for c in self.cells]
        yValues = [c.y for c in self.cells]
        return (min(xValues), min(yValues), max(xValues), max(yValues))

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

def makeBarChart(data):
    result = ""
    for i in range(0, len(data)):
        result += ("" + str(i) + "\t")
        if i in data:
            for dataPeice in data:
                if dataPeice == i:
                    result += "x"
        result += "\n"
    return result


if __name__ == "__main__":
    failureTimeData = []
    for a in range(100):
        grid = Grid()
        for i in range(0, 20):
            grid.addCellAt(random.randint(0, 10), random.randint(0, 10))
        x0, y0, x1, y1 = grid.bounds()
        outerBounds = (x0 - 1, y0 - 1, x1 + 1, y1 + 1)
        initial = grid.toString(outerBounds)
        previousGenerations = set()
        for i in range(1, 1000):
            gridAsCellSet = grid.cells
            if gridAsCellSet in previousGenerations:
                print("Repeats a previous generation on generation %s" % i)
                failureTimeData += [i]
                break
            previousGenerations.add(frozenset(gridAsCellSet))
            grid = grid.nextGeneration()
        if i == 999:
            print("Lasts the full 299 generations")
        failureTimeData += [90]
    print(failureTimeData)
    print(makeBarChart(failureTimeData))
