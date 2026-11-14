sum = 0

baso = True

while baso == True:
    x = int(input("Enter a number: "))

    if x == 0:
        print("loop is terminated")
        baso = False

    else:
        print("continue the loop")
        sum += x
        print("current sum is: ", sum)
        continue    