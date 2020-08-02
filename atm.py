
money = 10000

while True:
	print('--------------')
	print('กด 1: ถอนงิน')
	print('กด 2: เช็คยอดเงิน')
	print('กด q: ออกจากโปรแกรม')
	print('--------------')
	menu = input('กรุณาเลือกเมนู: ') # user เลือกแล้วเราจะเก็บเมนูไว้

	if menu == '1':
		print('<<< Withdraw >>>')
		withdraw = int(input('กรุณากรอกจำนวนเงิน: '))
		while withdraw > money:
			print('เงินในบัญชีไม่พอง่าย กรุณากรอกยอดเงินอีกครั้ง')
			withdraw = int(input('กรุณากรอกจำนวนเงิน: '))

		print('กรุณารับเงิน {} บาท'.format(withdraw))
		money = money - withdraw # เอาจำนวนเงินตอนนีมาลบกับเงินที่ถอน
		print('คงเหลือ: {} บาท'.format(money))

	elif menu == '2':
		print('ยอดเงิน: {} บาท'.format(money))

	elif menu == 'q':
		break

print('ขอบคุณที่ใช้บริการ กรุณารับบัตรคืน')
