a=int(input())
b=[int(a) for a in input().split()]
def solutionsets(b):
    result = b[0]
    for x in b:
        result |= x
    return result
result=solutionsets(b)
print(result)
