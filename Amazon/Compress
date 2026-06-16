s = input("Enter string: ")

result = ""
i = 0
while i < len(s):
    ch = s[i]
    count = 1
    while i + count < len(s) and s[i + count] == ch:
        count += 1
    result += ch + str(count)
    i += count
print("Compressed:", result)

compressed = result
output = ""
i = 0
while i < len(compressed):
    ch = compressed[i]
    num = ""
    i += 1
    while i < len(compressed) and compressed[i].isdigit():
        num += compressed[i]
        i += 1
    output += ch * int(num)
print("Decompressed:", output)
