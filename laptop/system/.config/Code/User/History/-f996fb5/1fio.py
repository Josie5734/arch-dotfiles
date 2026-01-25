# testing space 

text = "hello am text"

inputtype = str(type(text))

match inputtype:
    case "str":
        print("got it")
    case _: 
        print("not got it")