x = ['jeruk', 'apel', 'nanas', 'pir', 'melon', 'naga']
kiki = 6
for i, kiki in enumerate (x, 1):
    print(i, kiki)


x = 10

for i in range (x):
    if i == 4:
        x = x+1
        continue
    print(i)
    x = x+1
    
    