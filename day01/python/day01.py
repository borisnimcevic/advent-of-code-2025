start_position=50
current_position=start_position
one_counter = 0
two_counter = 0

with open("../input1.txt","r") as file:
# with open("../example.txt","r") as file:
    for line in file:
        directon=line[0]
        number=line[1:]
        if directon=='R':
            for x in range(int(number)):
                current_position+=1
                if(current_position>99):
                    two_counter+=1
                    current_position-=100
        else:
            for x in range(int(number)):
                current_position-=1
                if(current_position==0):
                    two_counter+=1
                if(current_position<0):
                    current_position+=100

        if(current_position==0):
           one_counter+=1

print(one_counter)
print(two_counter)
