import random

num = random.randint(1, 100)
guess = -1

print("我心里想了一个1到100之间的数字，请你来猜猜是多少？")

while guess != num:
    guess = int(input("你猜是哪个数？："))

    if guess == num:
        print("太棒了，你猜对了！")
        break
    elif guess < num:
        print("猜小了，再大胆一点！")
    else:
        print("猜大了，再小一点！")