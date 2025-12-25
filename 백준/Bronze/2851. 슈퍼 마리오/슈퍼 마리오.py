prefix_sum = 0
sum_arr = []

for _ in range(10):
    prefix_sum += int(input())
    sum_arr.append(prefix_sum)

for j in range(10):
    if sum_arr[j] >= 100:
        if j == 0:
            print(sum_arr[j])
        else:
            a = sum_arr[j]
            b = sum_arr[j-1]
            
            if a - 100 <= 100 - b:
                print(a)
            else:
                print(b)
        break
else:
    print(sum_arr[-1])
