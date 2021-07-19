# while True:
#     try:
#         word = map(str, input().lower())
#         count = [{i, 0} for i in range(25)]
#         print(count)

#         for ch in word:
#             num = ord(ch) - ord('a')
#             count[num].values() += 1

#         print([chr(ord(i)) for i in range(96, 96+26)] + ':' + count[i].values()
#               for i in range(25))
#     except EOFError:
#         break

# Using 'text' outside of while
text = ""
while True:
    try:
        tmp = input().lower()
        text = text+tmp
    except:
        break
for i in range(97, 97+26):
    print(chr(i), ":", text.count(chr(i)))
