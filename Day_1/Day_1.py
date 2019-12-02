import math
import copy

def calc_fuel(num_input):
    new_num = copy.copy(num_input)

    new_num = new_num // 3 
    new_num = math.floor(new_num)
    new_num -= 2
    return new_num



fp = open("Day_1.txt", 'r')

lines = fp.readlines()

#running_answer = 0
# for line in lines:
#     num = int(line)
#     num = num // 3 
#     num = math.floor(num)
#     num -= 2
    
#     running_answer += num

# print(running_answer)

running_answer2 = 0

for line in lines: 
    num = calc_fuel(int(line))
    
    while( num > 0 ):
        running_answer2 += num
        num = calc_fuel(num)
        print(num)

print(running_answer2)




