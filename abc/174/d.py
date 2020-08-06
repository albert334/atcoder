N = int(input())
c = list(input())
num_R = c.count("R")
num_R_2 = c[:num_R].count("R")
ans = num_R - num_R_2
print(ans)