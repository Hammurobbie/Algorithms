#!/usr/bin/python

import argparse


def find_max_profit(prices):

    cur_max = 0
    profit = 0

    for i in prices:
        for j in prices:
            if j > cur_max and prices.index(j) > prices.index(i):
                cur_max = j
                dif = cur_max - i
                if dif > profit:
                    profit = dif
        #     cur_min = i
        # if i > cur_max:
        #     cur_max = i
        # elif i < cur_min:
        #     cur_min = i
        #     if prices.index(cur_min) > prices.index(cur_max):
        #         print("fuck")

    print(f'max dif {cur_max}')
    print(f"A profit of {profit} can be made from the stock prices {prices}.")


find_max_profit([250, 1230, 100, 500, 2500, 50, 1000])


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
