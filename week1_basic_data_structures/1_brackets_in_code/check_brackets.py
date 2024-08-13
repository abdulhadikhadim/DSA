# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i + 1))

        elif next in ")]}":
            if not opening_brackets_stack:
                return i + 1

            # Process closing bracket
            top = opening_brackets_stack.pop()

            if top.char == '(' and next != ")":
                return i + 1
            if top.char == '{' and next != "}":
                return i + 1
            if top.char == '[' and next != "]":
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return None

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch:
        print(mismatch)
    else:
        print("Success")

if __name__ == "__main__":
    main()
