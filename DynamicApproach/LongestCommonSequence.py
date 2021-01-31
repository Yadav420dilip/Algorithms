"""The longest common subsequence problem is the problem of finding the longest subsequence common to all sequences
in a set of sequences. It differs from the longest common substring problem: unlike substrings, subsequences are not
required to occupy consecutive positions within the original sequences. """

"""For better understanding watch the video https://youtu.be/sSno9rV8Rhg"""


def lcs(string1, string2):
    m = len(string1)
    n = len(string2)

    l = [[None for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0

            elif string1[i - 1] == string2[
                j - 1]:  # check the alphabet of the 2 string match or not, in matrix indices are one extra therefore we reduce indices by 1
                l[i][j] = 1 + l[i - 1][
                    j - 1]  # if match the condition add diagonal value by 1 and store into the current index

            else:
                l[i][j] = max(l[i - 1][j],
                              l[i][j - 1])  # if not matches store the max value of the previous row and previous column

    return l


string1 = "BDCB"
string2 = "BACDB"

a = lcs(string1, string2)
print(a)
print("Longest Sequences ", a[-1][-1])

l1 = len(string1)
l2 = len(string2)

sequence = []
val = None

while val != 0:  # continue the loop until you reaches to the zero value
    if a[l1][l2] == a[l1][l2 - 1]:  # if the consecutive value of the same row is equal then reduce the column  by 1
        l2 -= 1
    else:
        # if the consecutive value of the same row is  not equal then reduce the column and row  by 1 to go to 1
        # level up
        val = a[l1 - 1][l2 - 1]
        sequence.insert(0, string2[l2 - 1])  # insert that value from where index goes up
        l1 -= 1
        l2 -= 1
print(sequence)
