#Day6 Questions on loops using functions like range break,continue

#Question1:Write a while loop to print all even numbers from 1 to 50
i=0
while i<50:
    if i % 2==0:
        print(i)
    i+=1
#Keep asking the user to input a number until they enter -1. Use break to stop the loop.
while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    print("You entered:", number)
#Printnumbers from 1 to 20, but skip numbers that are multiples of 3 using continue.
i=1
while i<=20:
    if i%3==0:
        i+=1
        continue
    print(i)
    i+=1
#Given a list of numbers, use a for loop to find the sum of all numbers.
list=[24,55,66,77,88,22,33,54,53,52]
sum=0
for i in list:
    sum+=i
print("The total sum of the given list of numbers is",sum)
#Write a program to search for a number in a list. If found, print "Found" and stop using break.
list=[24,55,66,77,88,22,33,54,53,52]
number=54
idx=0
for i in list:
    if i==number:
        print("found at index",idx)
        break
    print("finding...")
    idx+=1
nums = list(map(int, input("Enter the even number of elements: ").split()))

if len(nums) % 2 != 0:
    print("Enter an even number of elements")
else:
    mid = len(nums) // 2
    leftsum = sum(nums[:mid])
    rightsum = sum(nums[mid:])

    if leftsum < rightsum:
        print(1)
    elif leftsum > rightsum:
        print(-1)
    else:
        print(0)



