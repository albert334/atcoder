import collections

N = int(input())
judgement = []
for i in range(N):
    judgement.append(input())
c = collections.Counter(judgement)

order = ["AC", "WA", "TLE", "RE"]
for ans in order:
    print(ans + " x " + str(c[ans]))