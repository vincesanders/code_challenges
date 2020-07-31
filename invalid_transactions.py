from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        customers = {}
        invalid = set()
        # step through the transaction list
        for i in range(len(transactions)):
            # parse info from string
            name, time, amount, city = transactions[i].split(',')

            time = int(time)
            amount = int(amount)

            transaction = [name, time, amount, city, transactions[i]]

            if amount > 1000:
                invalid.add(transactions[i])

            if name not in customers:
                customers[name] = [transaction]
                continue
            # check for transactions in different city by same customer to see if time is within 60minutes.
            for j in range(len(customers[name])):
                if customers[name][j][3] != city and -60 <= time - customers[name][j][1] <= 60:
                    if customers[name][j][4] not in invalid:
                        invalid.add(customers[name][j][4])
                    invalid.add(transactions[i])

            customers[name].append(transaction)

        return list(invalid)


transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
transactions2 = ["alice,20,800,mtv","alice,50,1200,mtv"]
transactions3 = ["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]
transactions4 = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
transactions5 = ["lee,886,1785,beijing","alex,763,1157,amsterdam","lee,277,129,amsterdam","bob,770,105,amsterdam","lee,603,926,amsterdam","chalicefy,476,50,budapest","lee,924,859,barcelona","alex,302,590,amsterdam","alex,397,1464,barcelona","bob,412,1404,amsterdam","lee,505,849,budapest"]
transactions6 = ["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona","alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok","bob,188,989,amsterdam"]

solution = Solution()

# print(solution.invalidTransactions(transactions))
# print(solution.invalidTransactions(transactions2))
# print(solution.invalidTransactions(transactions3))
# print(solution.invalidTransactions(transactions4))
# print(solution.invalidTransactions(transactions5))
# print(f'expected: {["lee,886,1785,beijing","alex,763,1157,amsterdam","lee,924,859,barcelona","alex,397,1464,barcelona","bob,412,1404,amsterdam"]}')
print(solution.invalidTransactions(transactions6))