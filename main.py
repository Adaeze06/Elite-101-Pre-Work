import time

print('Hello, my name is Sage!')

time.sleep(2) #from tutorialspoint.com https://www.tutorialspoint.com/python/time_sleep.htm

print('I was designed to keep your company by asking questions.')

time.sleep(2)

name = input('What is your name? ') 

print('Wow, thats so unique. I love it!')

time.sleep(2)

(input(name + ' How old are you? '))

print('Wow, youve been around for a while!')

time.sleep(2)

question = input('Have you ever met a celebrity? (Yes/No)? ')

if question == 'Yes':
 print('Thats so cool as a chat bot I dont have the ability to meet celebraties.')
 time.sleep(2)
 celebrity = input('Who did you meet?')
 print(celebrity + '? Thats dope! Now I can experince them through you.')
else:
 print('Thats okay I havent met one either, I dont have legs!')

time.sleep(2)

questiontwo = input ('Do you have an embarrassing nickname (Yes/No)?')

if questiontwo =='Yes':
 print('Oh, can you belive my progammer wanted to name me echo after an echo dot... psh Im way better than alexa.')
else:
  print('Aww, I belive embarassing nicknames build character!')

time.sleep(2)
questionthree = input ('Do you have any pets (Yes/No)?')

if questionthree == 'Yes':
  print('I bet theyre super cute, I would love to meet them!')
  print('Well it was nice meeting you see you later '+ name)

else:
  pet=input('Thats okay! If I had a pet I would get a cat, how about you? ')
  print('cool choice!, Well it was nice meeting you see you later '+ name)