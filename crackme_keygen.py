summ =0
print "Type a user: "
user = raw_input()
lenght = len(user)

if(lenght > 0xb):
		exit()

userMAY=""

for i in range(lenght):
	if(ord(user[i]) < 0x41):
		print "Invalid char :("
		exit()
	if(ord(user[i]) > 0x5a):
		userMAY += chr(ord(user[i]) - 0x20)
	else:
		userMAY += chr(ord(user[i]))

print "USER: ", userMAY

for i in range(len(userMAY)):
	summ+=ord(userMAY[i])

print "SUM: ", hex(summ)

xorr = summ ^ 0x5678
print "XOR: ", hex(xorr)

total = xorr ^ 0x1234
print "PASS: ", total