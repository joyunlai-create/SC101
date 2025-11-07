"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random

def main():
	"""
	Generates coin flip results when number of runs hits the target given by the user.
	"""
	print('Let\'s flip a coin!')
	target_run = int(input('Number of Runs: '))

	next_run_switch = True
	current_run = 0
	overall_result = ''
	while current_run < target_run:
		result = random.choice(['H', 'T'])
		overall_result = overall_result + result
		if len(overall_result) == 1:
			pass
		else:
			current = overall_result[-1]
			previous = overall_result[-2]
			if current != previous:
				next_run_switch = True
			elif next_run_switch and current == previous:
				current_run += 1
				next_run_switch = False
	print(overall_result)





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
