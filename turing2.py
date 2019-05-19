accepted = True
tape = [0,0,0,0,1,1,1,]
head = int(len(tape) /2)
zero_marked= False
one_marked = False
unmarked_zero = False
unmarked_one = False
start = True
i = 0
while i <= int(len(tape) /2 ):

	if one_marked or start:
		while head >=  0: #mark 0
			if tape[head] == 0:
				unmarked_zero = False
				tape[head] = '0'
				zero_marked = True
				one_marked = False
				head_zero = head
				while(head_zero >= 0):
					if tape[head_zero] == 0:
						unmarked_zero = True
						break
					head_zero -= 1
				break
			head -=1 

	if zero_marked:
		while head <= len(tape) -1:
			if tape[head] == 1:
				unmarked_one = False
				tape[head] = '1'
				one_marked = True
				zero_marked= False
				head_one = head
				while(head_one <= len(tape) -1):
					if tape[head_one] == 1:
						unmarked_one = True
						break
					head_one += 1
				break
			head += 1
	if unmarked_zero and not unmarked_one:
		accepted = False
		break
	start = False
	if unmarked_zero and not unmarked_one or unmarked_one and not unmarked_zero:
		accepted = False
		break
	i += 1

print(tape)
print(accepted)


