my_list = [12, 45, 52, 12, 78, 52, 63, 95, 82, 0, -5, -7, -9, -7]
a = 0
while a <= len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
    a += 1
    if my_list[a] == 0:
        continue
    if my_list[a] < 0:
        break
