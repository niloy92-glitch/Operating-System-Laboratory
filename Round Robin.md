n = int(input("Enter number of processes: "))

p = []

for i in range(n):
    name = input("Process name: ")
    at = int(input("Arrival time: "))
    bt = int(input("Burst time: "))


    p.append([name, at, bt, bt, 0])

q = int(input("Quantum: "))

time = 0
done = 0
queue = []

while done < n:

    for i in range(n):
        if p[i][1] <= time and p[i][3] > 0 and i not in queue:
            queue.append(i)

    if not queue:
        time += 1
        continue

    i = queue.pop(0)

    run = min(q, p[i][3])
    time += run
    p[i][3] -= run

    for j in range(n):
        if p[j][1] <= time and p[j][3] > 0 and j not in queue and j != i:
            queue.append(j)


    if p[i][3] == 0:
        p[i][4] = time
        done += 1
    else:

        queue.append(i)


print("\nP\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for x in p:
    tat = x[4] - x[1]
    wt = tat - x[2]

    total_tat += tat
    total_wt += wt

    print(
        x[0], "\t",
        x[1], "\t",
        x[2], "\t",
        x[4], "\t",
        tat, "\t",
        wt
    )

print("\nAverage TAT =", total_tat / n)
print("Average WT =", total_wt / n)
