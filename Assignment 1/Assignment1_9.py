no = 10
i = 0

while no > 0:
	if i == 0:
		i += 1
	elif i % 2 == 0:
		print(i)
		no -= 1
		i += 1
	else:
		i += 1