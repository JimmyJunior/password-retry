password = input('請輸入你的新密碼:')
print('你最多只能輸入三次密碼')
x = 3
while x > 0:
	y = input('請輸入你的密碼:')
	if password == y:
		break
	else:
		x -= 1
		print("密碼錯誤")
		print("還有", x ,"次機會")
print("登入成功")		