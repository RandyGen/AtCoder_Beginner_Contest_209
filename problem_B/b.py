import sys

f = 0

for l in sys.stdin:
  if f == 0:
    n, x = l.split()
    n, x = int(n), int(x)
    f = 1
  else:
    li = l.split()
    li = [int(i) for i in li]
    s = sum(li)-(n//2)
    print('No' if s>x else 'Yes')
      