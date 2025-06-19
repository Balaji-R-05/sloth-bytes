# 11 Mar 2025

# Hidden Calculator Words
# Create a function that converts numbers into "calculator words" by mapping each digit to a corresponding letter or symbol, as if viewed upside-down on a calculator display.

# Digit-to-Letter Mapping

# | Digit | Letter/Symbol |
# |-------|:-------------|
# | 0     | O            |
# | 1     | I            |
# | 2     | Z            |
# | 3     | E            |
# | 4     | H            |
# | 5     | S            |
# | 6     | G            |
# | 7     | L            |
# | 8     | B            |
# | 9     | -            |

def turnCalc(num_str: str) -> str:
    numMap = {'1': "I", '2': "Z", '3': "E", '4': "H", '5': "S", '6': "G", '7': "L", '8': "B", '9': "-", '0': "O"}
    res = ""
    for ch in reversed(num_str):
        res += numMap.get(ch, "")
    return res

if __name__ == "__main__":
    print(turnCalc("707"))     
    print(turnCalc("5508"))    
    print(turnCalc("3045"))    
    print(turnCalc("07734"))   