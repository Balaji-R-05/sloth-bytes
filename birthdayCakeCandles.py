# 18 Jun 2025

# Birthday Cake Candles
# You are in charge of the cake for a child's birthday. The cake will have one candle for each year of their age.
# The child can only blow out the tallest candles.
# Your task is to count how many candles are the tallest.

def birthdayCakeCandles(candles):
    if not candles:
        return 0 
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == "__main__":
    print(birthdayCakeCandles([4,4,1,3]))
    print(birthdayCakeCandles([1, 1, 1, 1]))
    print(birthdayCakeCandles([]))