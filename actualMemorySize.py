# 28 May 2025

# The Actual Memory Size of Your USB Flash Drive
# Create a function that takes the memory size (ms) as an argument and returns the actual memory size.

def actualMemorySize(ms):
    value = float(ms[:-2])
    unit = ms[-2:].upper()
    
    # Apply 7% loss
    actual_value = value * 0.93

    if unit == "GB":
        if actual_value >= 1:
            return f"{round(actual_value, 2)}GB"
        else:
            return f"{round(actual_value * 1000)}MB"
    elif unit == "MB":
        return f"{round(actual_value)}MB"
    else:
        return "Invalid input"


res = actualMemorySize("32GB")
print(res)