number = int(input("Number:"))
count = 0
orig_number= number
while number !=1:
    if number % 2 == 0:
        number /=2
        print (number)
        count += 1
    else:
        number = number*3+1
        print (number)
        count += 1
print ("It took",count,"runs for",orig_number,"to go down to 1.")

# "My first python program, follows this http://www.someecards.com/life/school/collatz-conjecture/
