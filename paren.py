def paren(s, l, r, p, n):

    if p == 2 * n:
        print("".join(s))
        return


    if l < n:
        s[p] = "{"
        paren(s, l + 1, r, p + 1, n)

    if l > r:
        s[p] = "}"
        paren(s, l, r + 1, p + 1, n)

n = int(input("Enter number of parentheses: "))

s = [""] * (2 * n)

print("\nBalanced Parentheses:\n")

paren(s, 0, 0, 0, n)