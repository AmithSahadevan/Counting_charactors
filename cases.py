Input = input('Enter a sentance: ')	# Taking input.

lc = 0	# lowercase count
uc = 0	# uppercase count
sp = " ~`!@#$%^&*()\-_=+/]}{[" 	# possible special charactors
spc = 0	# special charactors count
dc = 0	# digits count

for i in Input:		#looping thru the letters in Input
	if i>="a" and i<="z":
		lc += 1
	if i>= "A" and i<="Z":				# Incrementing the counts
		uc += 1
	if i>= '0' and i<='9':
		dc += 1
	if i in sp:
		spc += 1
												# I'm using a formated string.
print(f"""The number of lower cases = {lc}
The number of upper cases = {uc}
The number of special charactors = {spc}		
The number of digits present = {dc}""")