from unittest import TestCase, main
from gameOfLife import *

class RulesTest(TestCase):
    def testThatCellWithNoNeighboursDies(self):
        self.assertFalse(Rules().shouldCellStayAlive(0))
        self.assertFalse(Rules().shouldCellStayAlive(1))
        self.assertFalse(Rules().shouldCellStayAlive(4))
        self.assertTrue(Rules().shouldCellStayAlive(2))
        self.assertTrue(Rules().shouldCellStayAlive(3))

    def testThatCellWithThreeNeighboursSpringsIntoLife(self):
        self.assertTrue(Rules().shouldCellSpringIntoLife(3))
        self.assertFalse(Rules().shouldCellSpringIntoLife(6))

class GridTest(TestCase):
    def testThatEmptyGridDoesNotContainAnyCells(self):
        self.assertFalse(Grid().isLiveCellAt(0, 0))

    def testThatGridWithCellContainsACell(self):
        testGrid = Grid()
        testGrid.addCellAt(0, 0)
        self.assertTrue(testGrid.isLiveCellAt(0, 0))

    def testThatGridCanTellHowManyNeighboursCellHasGot(self):
        testGrid = Grid()
        testGrid.addCellAt(5, 5)
        testGrid.addCellAt(10, 10)
        testGrid.addCellAt(11, 12)
        testGrid.addCellAt(12, 11)
        self.assertEquals(0, testGrid.numberOfNeighbours(0, 0))
        self.assertEquals(1, testGrid.numberOfNeighbours(5, 4))
        self.assertEquals(3, testGrid.numberOfNeighbours(11, 11))

    def testBounds(self):
        testGrid = Grid()
        testGrid.addCellAt(5, 7)
        testGrid.addCellAt(10, 4)
        self.assertEquals((5, 4, 10, 7), testGrid.bounds())

    def testThatGridCanMoveToNextGeneration(self):
        testGrid = Grid()
        testGrid.addCellAt(10, 10)
        testGrid.addCellAt(11, 10)
        testGrid.addCellAt(12, 10)
        testGrid = testGrid.nextGeneration()
        self.assertFalse(testGrid.isLiveCellAt(10, 10))
        self.assertTrue(testGrid.isLiveCellAt(11, 10))
        self.assertFalse(testGrid.isLiveCellAt(12, 10))

        self.assertTrue(testGrid.isLiveCellAt(11, 11))
        self.assertTrue(testGrid.isLiveCellAt(11, 9))

    def testThatGridCanBeDisplayed(self):
        testGrid = Grid()
        testGrid.addCellAt(2, 1)
        testGrid.addCellAt(1, 0)
        self.assertEquals("--x\n-x-\n", testGrid.toString((0, 0, 2, 1)))

    def testBoundsForEmptyGrid(self):
        testGrid = Grid()
        self.assertEquals((0,0,0,0), testGrid.bounds())

if __name__ == '__main__':
    main()
