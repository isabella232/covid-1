import math
import csv
from collections import defaultdict
import sys
import matplotlib.pyplot as plt
import numpy as np

POST_LEN = 8
MAX_CURVES = 5

def plot(target_curve, other_curves, num_points, county):
    # Make a data frame
    # create a color palette
    cmap = plt.get_cmap('hsv')
    colors = [cmap(i) for i in np.linspace(0, 1, len(other_curves))]
    
    x = [i for i in range(num_points)]
    num=0
    for cnt in other_curves:
        plt.plot(x, other_curves[cnt], marker='', color=colors[num], linewidth=1, alpha=0.9, label=cnt)
        # Add legend
        num+=1

    plt.plot(x[:num_points-POST_LEN], target_curve, marker='', color='orange',
             linewidth=4, alpha=0.7, label=county)

    # Add titles
    plt.legend(loc=2, ncol=2)
    plt.title("Growth", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Time")
    plt.ylabel("Number")
    plt.savefig(county + '.png')

    
def l2_norm(x, y):
    if len(x) != len(y):
        print(len(x), len(y))
        exit(1)
    diff = 0
    for i in range(len(x)):
        diff += (int(x[i])-int(y[i]))**2
    return diff

csv_r = csv.reader(open(sys.argv[1]))

by_country_list = defaultdict(list)
for r in csv_r:
    count_jh, count_who, count_ecdc = r[-3], r[-2], r[-1]
    if count_jh:
        count = count_jh
    elif count_who:
        count = count_who
    else:
        count = count_ecdc
    if count:
        by_country_list[r[0]].append(count)

csv_r = csv.reader(open(sys.argv[2]))
target_curve = []
for r in csv_r:
    if r[0]:
        target_curve.append(r[0])

target_len = len(target_curve)

country_count = 0


out_res = []

for cnt in by_country_list:
    for st in range(len(by_country_list[cnt]) - target_len - POST_LEN):
        diff = l2_norm(target_curve, by_country_list[cnt][st:st+target_len])
        out_res.append((diff, cnt, st))

out_res = sorted(out_res, key=lambda x:x[0])
csv_w = csv.writer(open(sys.argv[3] + ".csv", "w"))
csv_w.writerow(["", "SantaClara", "Start"] + target_curve + ['']*POST_LEN)
out_country = set([])

out_plots = {}

for i in range(len(out_res)):
    if country_count  >= MAX_CURVES:
        break
    diff = out_res[i][0]
    cnt = out_res[i][1]
    st = out_res[i][2]
    if cnt in out_country:
        continue
    country_count += 1
    print(out_res[i])
    out_country.add(cnt)
    csv_w.writerow([out_res[i][0], cnt,  str(st)] + by_country_list[cnt][st:st+target_len+POST_LEN])
    out_plots[cnt] = by_country_list[cnt][st:st+target_len+POST_LEN]
print("**********")     
plot(target_curve, out_plots, target_len+POST_LEN, sys.argv[3])
    
    
    
