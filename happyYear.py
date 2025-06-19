# 15 Apr 2025

# Next Happy Year
# A "Happy Year" is a year in which all digits are unique (no repeated digits).
# Create a function that takes an integer year and returns the next happy year.

def isHappy(num: int) -> bool:
    return len(set(str(num))) == len(str(num))

def happyYear(year: int) -> int:
    while True:
        year += 1
        if isHappy(year):
            return year
        
if __name__ == "__main__":
    res = happyYear(2021)
    print(res)