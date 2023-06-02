shoe_num = int(input())
sizes = input().split()
customers = int(input())

amount = []

total_set = [list(map(int, input().split())) for _ in range(customers)]

for x in range(customers):
    if str(total_set[x][0]) in sizes:
        amount.append(total_set[x][1])
        sizes.remove(str(total_set[x][0]))

print(sum(amount))
