import time
import random 

print('-'*65)
print('I am a Magic Eight ball!')
print()
question = input('Ask me a question! ')
time.sleep(0.7)
print('Shaking')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,6)

if choice ==1:
	print('I think so')
elif choice ==2:
	print('Nah man')
elif choice ==3:
	print('Ask later, too tired.')
elif choice ==4:
	print('Yeaaah')
elif choice ==5:
	print('Life is just a simulation.')
else:
	print('You will cease to exist in 5 seconds.')

