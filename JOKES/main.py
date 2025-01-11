import pyjokes
f=open('jokes.txt','w')

for i in range(1,51):
    f.write(str(i) + ' ')
    
    f.write(pyjokes.get_joke())
    f.write("\n\n")