s = input("Enter first string: ")
t = input("Enter second string: ")

rows = len(s)
cols = len(t)

dp = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(rows + 1):
    dp[i][0] = i
for j in range(cols + 1):
    dp[0][j] = j

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            insert_op = dp[i][j-1]
            delete_op = dp[i-1][j]
            replace_op = dp[i-1][j-1]
            dp[i][j] = 1 + min(insert_op, delete_op, replace_op)

print("Min operations:", dp[rows][cols])
