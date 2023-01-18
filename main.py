def year_profit(percent):
    return (money*percent)

per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
print('Please input your amount:')
money = int(input())/100
deposit = map(year_profit, per_cent.values())
print('The maximum about that you can earn is %s' % max(deposit))
























