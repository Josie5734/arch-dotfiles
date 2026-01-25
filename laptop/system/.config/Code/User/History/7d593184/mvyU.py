
text = "hello sidney"

while True:
    print(text)
    temp = text[0]
    text2 = None
    i = len(text)
    j = 1
    
    while j < i:
        text2 = text2 + text[j]
    text2 = text2 + temp
    text = text2

        