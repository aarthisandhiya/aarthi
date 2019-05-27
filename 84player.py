a=int(input())
b=[int(a) for a in input().split()]
def solution_sets(b):
    result = b[0]
    for x in b:
        result |= x
    return result
result=solution_sets(b)
print(result)
