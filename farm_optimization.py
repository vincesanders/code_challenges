'''
A farmer owns X acres of land. She profits P1 dollars per acre of corn and P2 dollars per acre of oats. Her team has Y hours of labor available. The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre. How many acres of each can be planted to maximize profits? Test the function for the following cases: 

a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2
'''

def farm_optimize(acres, labor_hours, corn_profit, oats_profit, corn_hours, oats_hours):
    # iterate backward from max corn acres till corn + oat land = corn + oat labor hours
    corn = acres
    oats = 0

    # find the point of intersection of c + o = acres and ch + oh = labor
    while corn_hours * corn + oats_hours * oats != labor_hours:
        # corn + oats will always equal acres, we want to utilize all land and labor
        # We want to find the ratio of corn to oats that also utilizes all labor
        corn -= 1
        oats += 1

    # We have optimized acres
    # find profit
    return corn * corn_profit + oats * oats_profit

class Test:
    def __init__(self, acres, labor, corn_profit, oats_profit, corn_hours, oats_hours):
        self.acres = acres
        self.labor = labor
        self.corn_profit = corn_profit
        self.oats_profit = oats_profit
        self.corn_hours = corn_hours
        self.oats_hours = oats_hours

test_1 = Test(240, 320, 40, 30, 2, 1)
test_2 = Test(300, 380, 70, 45, 3, 1)
test_3 = Test(180, 420, 65, 55, 3, 2)

optimized_test_1 = farm_optimize(test_1.acres, test_1.labor, test_1.corn_profit, test_1.oats_profit, test_1.corn_hours, test_1.oats_hours)
optimized_test_2 = farm_optimize(test_2.acres, test_2.labor, test_2.corn_profit, test_2.oats_profit, test_2.corn_hours, test_2.oats_hours)
optimized_test_3 = farm_optimize(test_3.acres, test_3.labor, test_3.corn_profit, test_3.oats_profit, test_3.corn_hours, test_3.oats_hours)

print(optimized_test_1)
print(optimized_test_2)
print(optimized_test_3)