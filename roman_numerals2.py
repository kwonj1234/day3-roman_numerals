def arab_to_rom(num):
    #roman numeral translation
    roman = {1: "I", 4: "IV", 5:"V", 9:"IX", 10:"X", \
        40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", \
            500:"D", 900:"CM",1000:"M"}
    
    #convert input number into string and reverse it
    #so that when you iterate over the number you start at the 
    #ones place
    string_num = str(num)
    reverse = string_num[::-1]
    #retrieve the number of digits in the input
    digits = len(string_num)
    #base 10 list
    place = [1,10,100,1000]

    #initialize output 
    output = []

    #separate original number by place value
    for i in range(0, digits):
        output.append(int(reverse[i])*place[i])
    print(output)

arab_to_rom(345)
