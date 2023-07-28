from hashlib import new


import random
s = "zeellukhi99@gmail.com"
news = s.rpartition('@')
print(news[0])
l =list(news[0])
random.shuffle(l)
answer =''.join(l)
print(answer + "@gmail.com")