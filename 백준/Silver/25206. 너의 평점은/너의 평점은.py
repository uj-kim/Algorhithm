dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

sub_sum = 0
crd_sum = 0

for i in range(20):
  sub, credit, grade = input().split()

  if grade != 'P':
    crd_sum += float(credit)
    sub_sum += float(credit) * dic[grade]
  
print(round(sub_sum / crd_sum, 6))