while True:
  n = int(input())
  
  if n == -1:
    break

  q = [i for i in range(1, n+1) if n % i == 0]
  
  if sum(q[:-1]) ==  n:
    print(f"{q[-1]} = {' + '.join(map(str,q[:-1]))}")
  else:
    print(f"{n} is NOT perfect.")

