# 18 Jun 2025

def birthdayCakeCandles(candles):
    if not candles:
        return 0 
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == "__main__":
    print(birthdayCakeCandles([4,4,1,3]))
    print(birthdayCakeCandles([1, 1, 1, 1]))
    print(birthdayCakeCandles([]))