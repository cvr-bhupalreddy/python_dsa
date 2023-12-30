
mylist = [1,2,3,4]

print(mylist)

mytuple = (1,"string",3,4)

squarelist = [ element*element for element in mylist]


print(squarelist)

print(mytuple)




# This code runs only in python 3.10 or above versions
def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"


head = number_to_string(2)
print(head)