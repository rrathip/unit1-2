
print('What is your name?')
name = input()

print('Enter radius or length of your pool in feet?(assuming height of 6),', name)
a = int(input())
print('If your pool is rectangular enter its other side length,', name)
b = int(input())
print((a**2)*3.14*7.5*6, "is your pool's volume in gallons for a cylindrical pool,", name)
print(a**2*7.5*6, "is your pool's volume in gallons for a square pool,", name)
print(a*b*6*7.5, "is your pool's volume in gallons for a rectangular pool,", name)


print("Name the 4 individuals to calculate?")
name1 = (input())
name2 = (input())
name3 = (input())
name4 = (input())
print("List the GPA of each member")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = a + b + c + d
print(x/4, "is the average GPA of", name1, ",",  name2, ",", name3, "and", name4)


print('Enter a 2 digit number to swap')
x = int(input())
y = (x%10)*10
z = (x - (x%10))/10
print(int(y + z))


print('Enter the year')
x = int(input())
y = int((x/100)+1)
if x%1000==0:
    print(int(x/100))
else:
    print(y, "century")
    
    
    
print('Enter the values of H, A, and B respectively')
h = int(input())
a = int(input())
b = int(input())
n = a-b
print(float(h/n), "days")


print("Enter the day in question")
x = int(input())

print(((x%7)+3)%7)
