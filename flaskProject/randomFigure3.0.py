import random

print("猜数字游戏3.0")
# 设置随机数字范围和剩余猜测次数
start = 1
end = 20
guesses_left = 5
# 生成随机数字
secret_number = random.randint(start, end)
# 开始猜数字
print(f"我想了一个 {start} 到 {end} 之间的数字，你有 {guesses_left} 次机会猜测。")
while guesses_left > 0:
    guess = int(input("请猜一个数字："))
    guesses_left -= 1

    if guess < secret_number:
        print("你输入的数字猜小了，请再输一次。")
    elif guess > secret_number:
        print("你输入的数字猜大了，请再输一次。")
    else:
        print(f"恭喜你，猜对了！我想的数字是 {secret_number} 。")
        break

    if guesses_left > 0:
        print(f"你还有 {guesses_left} 次机会。")
    else:
        print(f"很遗憾，你没有猜对。我想的数字是 {secret_number} 。")