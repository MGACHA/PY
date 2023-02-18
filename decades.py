age = int(input ("how old are you?\n"))
decades = age//10
years =  age % 10
days = decades - years//365
print("you are "+ str(decades) + "decades and" + str(days) + "years old.")