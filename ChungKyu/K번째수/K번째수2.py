



def hap(x,y):
    return  x + y

print(hap(10,20))

(lambda x,y: x+y)(10,20)

# a =list(map(lambda x: x ** 2, range(5)))
# print(a)

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

