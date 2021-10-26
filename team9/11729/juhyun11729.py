n = int(input())
count = 0
move_arr = []
def hanoi(n, from_pos, to_pos, aux_pos):
    global count
    count += 1
    if n==1:
        move_arr.append(str(from_pos)+' '+str(to_pos))
        return
    hanoi(n-1,from_pos,aux_pos,to_pos)
    move_arr.append(str(from_pos) + ' ' + str(to_pos))
    hanoi(n-1,aux_pos,to_pos,from_pos)

hanoi(n,1,3,2)
print(count)
for v in move_arr:
    print(v)