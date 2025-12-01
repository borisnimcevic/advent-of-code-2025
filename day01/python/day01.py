start_position=50
current_position=start_position
counter = 0

with open("example.txt","r") as file:
    for line in file:
        directon=line[0]
        number=line[1:]
        if directon=='R':
            current_position+=int(number)
            if(current_position>99):
                current_position-=100
        else:
            current_position-=int(number)
            if(current_position<0):
                current_position+=100

        if current_position==0:
            counter+=1

        # print(directon,end="")
        # print()
        # print(number,end="")
        # print()
        # print(current_position,end="")
        # print()

print(counter)
