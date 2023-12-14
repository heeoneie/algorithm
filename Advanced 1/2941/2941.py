alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for char in alpha:
       word = word.replace(char,'*')
print(len(word))
