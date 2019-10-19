"""
Problem Definition:   Read Text Justification problem from internet resource. Write a python code to implement text justification problem.

"""

import time
def fullJustify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        # Check if the word to be checked crosses the max width or not
        if len(w) > maxWidth:
            print("Increase the maxWidth")
            return ""
        # Check if the word can be added in the ongoing line or not
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]


if __name__ == '__main__':
    print("Text Justification Problem Implementation:\n")
    # Test Case 1
    s = input("Enter the text to be justified\n")#"Sample text for Text Just problem"
    mWidth = int(input("Enter the max width.\n"))

    l = fullJustify(s.split(), mWidth)
    for i in l:
        print(i + "\n")
    time.sleep(10)

