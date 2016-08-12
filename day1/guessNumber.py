lucky_number = 12
count = 6

while (count>0):

    input_number = (int)(input("please input a number from 0 t 100:"))
    count = count - 1

    if input_number<lucky_number:
        print("the lucky number is bigger")
    elif input_number>lucky_number:
        print("the lucke number is smaller")
    else:
        print("bingo")
        break

else:
    print("you have no chance")