

'''
f = open("sampletext.txt", "a")
x = f.write("reinhart christian g. caspe\n")
f.close()

f = open("sampletext.txt", "r")
print(f.read())
'''

'''
f = "sampletext.txt"
with open(f, "w") as y:
    y.write("id1010101 Reinhart Christian Caspe")

f = open("sampletext.txt", "r")
print(f.read())
f.close()

'''

'''
f = open("sampletext.txt", "r")
x = f.read()
y = input("what you are looking: ")

if y in x:
    print(x)
    print("I found it here")
else:
    print("sorry")

'''

'''
f = open("sampletext.txt", "r")
x = f.read()
y = input("What you are looking for: ")
i = x.find(y)

print(i)

'''

'''import pandas

df = pd.read_csv(r'myfile.csv')
print(df)'''


