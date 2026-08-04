process = [
    ["p1", 1, 1],
    ["p2", 2, 3],
    ["p3", 3, 3],
    ["p4", 5, 2]
]


process.sort(key=lambda x: x[1])

ct = 0
total_TAT=0
total_WT=0

for p in process:
    if current < p[1]:
        current = p[1]

    ct += p[2]
    p.append(ct)
    p.append(p[3] - p[1])
    p.append(p[4] - p[2])

    total_TAT += p[4]
    total_WT += p[5]

print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in process:
    print(*p, sep="\t")

avg_TAT= total_TAT/len(process)
avg_WT = total_WT/len(process)

print(avg_TAT)

print(avg_WT)

