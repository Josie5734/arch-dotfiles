
text = "hello sidney"

while True:
    print(text)
    temp = text[0]
    i = text.len()
    j = 0
    for char in text:
        text[i] = text[j]
        i -= 1
        j += 1
        