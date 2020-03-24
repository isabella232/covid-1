import csv
import sys

csv_r = csv.reader(open(sys.argv[1]))
head = True
for r in csv_r:
    if head:
        head=False
        continue
    code = r[0]
    county = r[1].replace(" ", "_").lower()
    state = r[2]
    count_arr = r[-20:-1]
    total_count = sum([int(x) for x in count_arr])
    fname = str(total_count) + "_" + county + "_" + state + ".csv"
    with open(fname, "w") as f:
        for c in count_arr:
            f.write(str(c))
            f.write("\n")
    
