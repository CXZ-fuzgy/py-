name = input("请输入姓名：")
age = input("请输入年龄：")

print(f"姓名：{name}   年龄{age}")
#---- 进入系统年龄判断 <17 可进入系统 ----
try:
    age_num = int(age)
    if age_num>=18:
        print("你可以参加活动")
    else:
        print("您是未成年，不可以参加活动哦。")
        exit()
except ValueError:
    exit()
#---- D4：whlie 循环做密码验证（有次数限制）----
print("----输入密码进入系统----")
Correct_password = "38979471"   #正确密码
attempt_count = 0               #尝试次数
max_attempts = 4                #最大次数

while attempt_count < max_attempts:
    enter_passwork = input(f'（你还有{max_attempts-attempt_count}次)请输入密码')
    if enter_passwork == Correct_password:
        print("输入正确！")
        print("----欢迎进入系统----")
        break
    else:
        attempt_count += 1
        print(f"密码错误!(你还剩{max_attempts-attempt_count}次)")
#循环结束后，检测是因为输对了跳出，还是次数用完了
if attempt_count == max_attempts:
    print("错误次数过多，账号锁定！")
