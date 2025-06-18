def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]

    min_coins = [0] + [float('inf')] * amount
    last_coin = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

 
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result


if __name__ == "__main__":
    test_amount = 113
    print("Greedy:", find_coins_greedy(test_amount))
    print("DP:", find_min_coins(test_amount))
