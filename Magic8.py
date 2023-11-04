#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
name = input()
question = "Welcome, Are you enjoying your python lesson"
answer = ""
if name == "":
  print(question)
else:
  print(name, question)
random_number = random.randint(1, 12)

if random_number == 1: 
  answer = "Yes - definitely"
elif random_number == 2: 
  answer = "It is decidedly so"
elif random_number == 3: 
  answer = "Without a doubt"
elif random_number == 4: 
  answer = "Reply hazy, try again"
elif random_number == 5: 
  answer = "Ask again later"
elif random_number == 6: 
  answer = "Better not tell you now"
elif random_number == 7: 
  answer = "My sources say no"
elif random_number == 8: 
  answer = "Outlook not so good"
elif random_number == 9: 
  answer = "Very doubtful"
elif random_number == 10: 
  answer = "I am making a lot of progress"
elif random_number == 11: 
  answer = "I am the next big thing in the US"
elif random_number == 12: 
  answer = "You can't believe it but I have gotten a job!"
else:
  answer = "Error"
print("Magic 8-Ball's answer:", answer)

