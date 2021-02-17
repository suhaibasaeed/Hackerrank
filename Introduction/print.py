"""
The included code stub will read an integer,n, from STDIN.

Without using any string methods, try to print the following:

123...n

Note that "..." represents the consecutive values in between.
"""

if __name__ == '__main__':
    n = int(input())
    # Create list of numbers
    lst = list(range(1, n+1))

    new_str = ""
    # Loop through list of no's and append to the empty string
    for i in lst:
        new_str += str(i)

    print(new_str)