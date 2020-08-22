import collections
n = int(input())
s = [input() for i in range(n)]
d = collections.Counter(s)
largest = max(d.values())
ans = []
for key in d.keys():
    if d[key] == largest:
        ans.append(key)
common_values = sorted(ans)
for val in common_values:
    print(val)
