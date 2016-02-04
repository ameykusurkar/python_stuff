import sys
import operator

if len(sys.argv) is 1:
    exit()

f = open(sys.argv[1], 'r')

words = f.read().split()

total = 0
counts = {}

for word in words:
    total += 1
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

def print_dict(d):
    sorted_vals = sorted(d.items(), key=operator.itemgetter(1))
    for pair in sorted_vals:
        print pair

print_dict(counts)
print '{} words'.format(total)
