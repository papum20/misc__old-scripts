def f(b) :
	c = 0	#count
	l = []	#letters
	for i in range(len(b)) :
		if b[i] not in l and b.count(b[i]) %2 == 1 :
			l.append(b[i])
			c += 1
		if c > 1 :
			return "it isn't an anandrome\n\n"
	return "it's an anandrome!\n\n"

while True :
	print(f(input("insert a string: ")))