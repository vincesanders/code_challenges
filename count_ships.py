# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def __init__(self, x: int, y: int):
        self.hasShipCount = 0
        self.matrix = []
        for i in range(x):
            column = []
            for j in range(y):
                column.append(0)
            self.matrix.append(column)
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        self.hasShipCount += 1
        for i in range(bottomLeft.x, topRight.x + 1):
            for j in range(bottomLeft.y, topRight.y + 1):
                if self.matrix[i][j] == 1:
                    return True

    def addShip(self, x, y):
        self.matrix[x][y] = 1

class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'

# break each rectangle in fours
# if it does't have ships stop
# if it does, divide again until 1 unit long
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        # check if have ships and make sure we haven't gotten smaller than a single point
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y or not sea.hasShips(topRight, bottomLeft):
            return 0
    
        # We got past the first condition, so point found
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        # break each rectangle in fours
        dividing_vertical = (topRight.x + bottomLeft.x) // 2
        dividing_horizontal = (topRight.y + bottomLeft.y) // 2
        
        total = 0
        total += self.countShips(sea, Point(dividing_vertical, dividing_horizontal), bottomLeft)
        total += self.countShips(sea, topRight, Point(dividing_vertical + 1, dividing_horizontal + 1)) 
        total += self.countShips(sea, Point(dividing_vertical, topRight.y), Point(bottomLeft.x, dividing_horizontal + 1)) 
        total += self.countShips(sea, Point(topRight.x, dividing_horizontal), Point(dividing_vertical + 1, bottomLeft.y))
        
        return total


sea = Sea(10000, 10000)

points = [[53,118],[373,246],[121,625],[805,303],[383,532],[982,664],[453,122],[347,106]]

for i in range(len(points)):
    sea.addShip(points[i][0], points[i][1])
# sea.addShip(1,1)
# sea.addShip(5,5)
# sea.addShip(2,2)
# sea.addShip(3,3)

solution = Solution()

print(solution.countShips(sea, Point(1000, 1000), Point(0,0)))
print(sea.hasShipCount)