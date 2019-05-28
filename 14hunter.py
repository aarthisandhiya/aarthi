def permutations_with_repetition(s):
    base = len(s)
    for n in range(1,base**base):
        yield "".join(s[n // base**(base-d-1) % base] for d in range(0,base))
        #print(base)

s=input()
for p in permutations_with_repetition(s):
    print(p)

