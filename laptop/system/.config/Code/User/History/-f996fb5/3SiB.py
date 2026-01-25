# testing space 

text = "hello am text"

inputtype = type(text)

print(inputtype)

match inputtype:
    case "str":
        print("got it")
    case _: 
        print("not got it")