# 6 May 2025

# No Yelling

# Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.

def noYelling(s: str) -> str:
    if s.endswith("!") or s.endswith("?"):
        last_char = s[-1]
        s = s.rstrip(last_char)
        return s + last_char
    return s

if __name__ == "__main__":
    print(noYelling("What went wrong?????????"))       # ➜ What went wrong?
    print(noYelling("Oh my goodness!!!"))              # ➜ Oh my goodness!
    print(noYelling("I just!!! can!!! not!!! believe!!! it!!!"))  # ➜ unchanged
    print(noYelling("Oh my goodness!"))                # ➜ Oh my goodness!
