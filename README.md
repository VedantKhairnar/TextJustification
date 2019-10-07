# Text Justification Problem


## Problem Definition:

Read Text Justification problem from internet resource. Write a python code using
                        dynamic programming to implement text justification problem.
## Logic:

        1.a.First create list, with each index having one space separated word and less than maxWidth.
        1.b.Then Iterate over this new list to add more space by calculating quotient and remainder to add remaining spaces.
        2.a.Format the data into nested list format such that each element is a list having words in that line
        2.b.and simultaneously update the white space distribution

## Code

```
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

```

# Output:

Text Justification Problem Implementation:

Sample  

text for

Text    

Just    

problem 


* * 
# ***Developer Details:***

## Vedant Khairnar

  Cyber Security and Machine Learning Enthusiast

Website: https://vedantkhairnar.ml/

Linkedin: https://www.linkedin.com/in/vedantkhairnar/

Github: https://github.com/VedantKhairnar

HackerRank: https://www.hackerrank.com/Kingsmanvk?hr_r=1
