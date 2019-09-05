"""
Problem Definition:     Read Text Justification problem from internet resource. Write a python code using
                        dynamic programming to implement text justification problem.

Logic:
        a.First create list, with each index having one space separated word and less than maxWidth.
        b.Then Iterate over this new list to add more space by calculating quotient and remainder to add remaining spaces.

        a.Format the data into nested list format such that each element is a list having words in that line
        b.and simultaneously update the white space distribution
"""


def fullJustify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0

    for w in words:
        if len(w) > maxWidth:
            print("Increase the maxWidth")
            return ""
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    #  print(cur,num_of_letters,w)
    # print(res)
    return res + [' '.join(cur).ljust(maxWidth)]


if __name__ == '__main__':
    print("Text Justification Problem Implementation:\n")
    # Test Case 1
    s = "Sample text for Text Just problem"
    mWidth = 8

    l = fullJustify(s.split(), mWidth)
    for i in l:
        print(i + "\n")

    # Test Case 2
    # l=fullJustify("".split(),40)
    # s= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.".split()

"""

    flag = True
    for i in s.split():
        if len(i) > mWidth:
            flag = False
            print("Increase the maxWidth")
            break

    if flag == True:
        l = fullJustify(s.split(), mWidth)
        for i in l:
            print(i + "\n")

"""
