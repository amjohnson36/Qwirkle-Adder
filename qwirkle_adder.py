def qwirkle_adder():
	from operator import itemgetter

	"""Adds player scores for game Qwirkle"""

	print('I will add up the player scores for the game Qwirkle!')
	print('Add an "!" at the end of your points if you get a Qwirkle.')
	print('Type "q" once the game is finished up!\n')

	d = {}
	number_of_players = input('How many players? ')
	print('')
	for i in range(int(number_of_players)):
		name = input('Who is playing? ')
		d[name] = 0
		print('')

	d_qwirk = d.copy() # Keeps track of number of qwirkles
	
	running = True

	while running:
		try:
			for key, value  in d.items():
				points = input("How many points did you earn, {0}? ".format(key))
				if points.lower() == 'q':
					running = False
					break

				elif '!' in points.lower():
					print('Nice Qwirkle!')
					d_qwirk[key] += 1
				
				points = points.translate({ord(c): None for c in '!'})
				d[key] += int(points)
				print("Total points for " + key + ": " + str(d[key]) + '\n')
				
				
		except ValueError:
			print('Invalid number \n')
	
	winner = max(d.items(), key=itemgetter(1))[0]
	most_points = max(d.items(), key=itemgetter(1))[1]
	winners_qwirkles = d_qwirk[winner]

	print('\nCongratulations {0}! You won with {1} points and {2} qwirkles!\n'.format(winner, most_points, winners_qwirkles))
	
	for k, v in d.items():
		print(k + ' had ' + str(v) + ' points and ' + str(d_qwirk[k]) + ' qwirkles')

qwirkle_adder()
