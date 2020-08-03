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
    def __init__(self):
        self.checked_points = set()

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If this division of sea has ships, we divide it further
        if sea.hasShips(topRight, bottomLeft):
            if self.getWidth(topRight, bottomLeft) == 1 and self.getHeight(topRight, bottomLeft) == 1:
                total = 0
                # We're down to the smallest division
                topLeft_coords = (bottomLeft.x, topRight.y)
                topRight_coords = (topRight.x, topRight.y)
                bottomRight_coords = (topRight.x, bottomLeft.y)
                bottomLeft_coords = (bottomLeft.x, bottomLeft.y)

                bottomRight = Point(topRight.x, bottomLeft.y)
                topLeft = Point(bottomLeft.x, topRight.y)
                if topRight_coords not in self.checked_points:
                    self.checked_points.add(topRight_coords)
                    if sea.hasShips(topRight, topRight):
                        total += 1
                if bottomRight_coords not in self.checked_points:
                    self.checked_points.add(bottomRight_coords)
                    if sea.hasShips(bottomRight, bottomRight):
                        total += 1
                if bottomLeft_coords not in self.checked_points:
                    self.checked_points.add(bottomLeft_coords)
                    if sea.hasShips(bottomLeft, bottomLeft):
                        total += 1
                if topLeft_coords not in self.checked_points:
                    self.checked_points.add(topLeft_coords)
                    if sea.hasShips(topLeft, topLeft):
                        total += 1
                return total
            elif self.getWidth(topRight, bottomLeft) > 1 and self.getHeight(topRight, bottomLeft) == 1:
                # Width is still too long, divide in two length-wise
                dividing_point = ((topRight.x - bottomLeft.x) // 2) + bottomLeft.x
                left_topRight = Point(dividing_point, topRight.y)
                # left bottomLeft is same as bottomLeft
                # right topRight is same as topRight
                right_bottomLeft = Point(dividing_point, bottomLeft.y)

                return self.countShips(sea, left_topRight, bottomLeft) + self.countShips(sea, topRight, right_bottomLeft)
            elif self.getWidth(topRight, bottomLeft) == 1 and self.getHeight(topRight, bottomLeft) > 1:
                # Height is still too long, divide in two height wise
                dividing_point = ((topRight.y - bottomLeft.y) // 2) + bottomLeft.y # 1
                # top topRight is same as topRight
                top_bottomLeft = Point(bottomLeft.x, dividing_point)
                bottom_topRight = Point(topRight.x, dividing_point)
                #bottom bottomLeft is same as bottomLeft

                top = self.countShips(sea, topRight, top_bottomLeft)
                bottom = self.countShips(sea, bottom_topRight, bottomLeft)
                return top + bottom
            elif self.getWidth(topRight, bottomLeft) < 1 or self.getHeight(topRight, bottomLeft) < 1:
                return 0
            else:
                # Height and width still need to be divided
                # divide into four
                dividing_vertical = ((topRight.x - bottomLeft.x) // 2) + bottomLeft.x
                dividing_horizontal = ((topRight.y - bottomLeft.y) // 2) + bottomLeft.y

                topLeft_topRight = Point(dividing_vertical, topRight.y)
                topLeft_bottomLeft = Point(bottomLeft.x, dividing_horizontal)

                topLeft = self.countShips(sea, topLeft_topRight, topLeft_bottomLeft)

                # topRight topRight is same as topRight
                centerPoint = Point(dividing_vertical, dividing_horizontal)

                topRight_division = self.countShips(sea, topRight, centerPoint)

                # bottomLeft bottomLeft is same as bottomLeft

                bottomLeft_division = self.countShips(sea, centerPoint, bottomLeft)

                bottomRight_topRight = Point(topRight.x, dividing_horizontal)
                bottomRight_bottomLeft = Point(dividing_vertical, bottomLeft.y)

                bottomRight = self.countShips(sea, bottomRight_topRight, bottomRight_bottomLeft)
                
                return topLeft + topRight_division + bottomLeft_division + bottomRight
        else:
            # add exterior points to checked_points
            for i in range(bottomLeft.x, topRight.x + 1):
                # top points
                self.checked_points.add((i, topRight.y))
                # bottom points
                self.checked_points.add((i, bottomLeft.y))
            for i in range(bottomLeft.y, topRight.y + 1):
                # left points
                self.checked_points.add((bottomLeft.x, i))
                # right points
                self.checked_points.add((topRight.x, i))
            return 0

    def getArea(self, topRight, bottomLeft):
        return self.getWidth(topRight, bottomLeft) * self.getHeight(topRight, bottomLeft)

    def getWidth(self, topRight, bottomLeft):
        return topRight.x - bottomLeft.x

    def getHeight(self, topRight, bottomLeft):
        return topRight.y - bottomLeft.y
        

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