x=0.1
format(x,'.25f')

def f1(X):
    R=3
    return ((R+1)*X-R*(X*X))

def f2(X):
    R=3
    return ((R+1)*X-(R*X)*X)

x=0.5
y=0.5

for i in range(0,500):
    x=f1(x)
    y=f2(y)

print(x)
print(y)