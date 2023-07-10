# """ 1-Basic """
for i in range(0,151):
    print(i);

# """ 2 Multiple of 5"""

for i in range(5,1001,5):
    print(i)

# Counting,the Dojo Way
for i in range(1,101,):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)
Countdown by Fours
for i in range(2018,0,-4):
    print(i)
# flexible Counter
def count(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i %mult == 0:
            print(i)


count(2,19,3)