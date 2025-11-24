n_titans, s_muralha = map(int, input().split(" "))
seq_titans = list(input())
p, m, g = map(int, input().split(" "))

nmd = 1
ms = [s_muralha]
cm = s_muralha
for s in seq_titans:
    sz = 0

    if s == 'P':
        sz = p

    if s == 'M':
        sz = m

    if s == 'G':
        sz = g

    should_add = True
    for idx, mi in enumerate(ms):
        if mi > sz:
            ms[idx] = mi - sz
            should_add = False
            break;

    if should_add:
        ms.append(s_muralha - sz)


output = len(ms) -1 if ms[-1] == s_muralha else len(ms)
print(output)

