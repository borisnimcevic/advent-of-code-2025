start_position=50
current_position=start_position
counter = 0

with open("../input1.txt","r") as file:
# with open("../example.txt","r") as file:
    for line in file:
        directon=line[0]
        number=line[1:]
        if directon=='R':
            current_position+=int(number)
        else:
            current_position-=int(number)
        
        current_position%=100

        if current_position==0:
            counter+=1

        # print(directon,end="")
        # print()
        # print(number,end="")
        # print()
        # print(current_position,end="")
        # print()

print(counter)
