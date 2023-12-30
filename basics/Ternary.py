
def ternaryTest(a, b):
    result = "A and B are Equal " if a == b  else "A is Greater than B " if a > b else "A is less than B"
    return result

def reverseString(input):
    return input[ ::-1]



if __name__ == "__main__":

    print(reverseString("bhupal"))

    print(ternaryTest(10,5))
    print(ternaryTest(6,8))
    print(ternaryTest(5,5))