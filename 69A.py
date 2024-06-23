def is_in_equilibrium(n, forces):
    sum_x = sum_y = sum_z = 0
    
    for force in forces:
        sum_x += force[0]
        sum_y += force[1]
        sum_z += force[2]
    
    if sum_x == sum_y == sum_z == 0:
        return "YES"
    else:
        return "NO"

n = int(input().strip())  
forces = [list(map(int, input().strip().split())) for i in range(n)]  


print(is_in_equilibrium(n, forces))
