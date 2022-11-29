# create password generator

import random
import string

'''
2 upper case letter
2 lower case letter
2 number
2 punctuation
'''

sl = "abcdefghijklmnopqrstuvwxyz"
su = (sl).upper()
p = "!@#$%^&*()\/:|<>?"

p1 = random.choice(sl)
p2 = p1 + random.choice(sl)
p3 = p2 + str(random.randint(0, 9))
p4 = p3 + random.choice(su)
p5 = p4 + random.choice(p)
p6 = p5 + random.choice(su)

print(''.join(random.sample(p6,len(p6))))
