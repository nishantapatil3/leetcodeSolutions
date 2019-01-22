#py2

a = [-2, -3, 4, -1, -2, 1, 5, -3]

max_so_far = a[0]
max_till_here = 0

for each in a:
    max_till_here = max_till_here + each

    if max_so_far < max_till_here:
        max_so_far = max_till_here
    if max_till_here < 0:
        max_till_here = 0

print max_so_far
