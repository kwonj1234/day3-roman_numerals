#exercise 1

#convert a number into roman numerals
def arab_to_rom(num):
    #roman numeral translation
    # roman = {1: "I", 4: "IV", 5:"V", 9:"IX", 10:"X", \
    #     40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", \
    #         500:"D", 900:"CM",1000:"M"}
    
    #convert input number into string and reverse it
    #so that when you iterate over the number you start at the 
    #ones place
    string_num = str(num)
    reverse = string_num[::-1]

    #retrieve the number of digits in the input
    digits = len(string_num)
    print(reverse)

    #initialize output 
    output = []

    for i in range(0,digits):

        #sort the ones place
        if i == 0:
            if int(reverse[i]) < 4:
                output.append("I"*int(reverse[i]))
            elif int(reverse[i]) == 4:
                output.append("IV")
            elif int(reverse[i]) == 5:
                output.append("V")
            elif int(reverse[i]) < 9 and int(reverse[i]) > 5:
                output.append("I"*(int(reverse[i])-5))
                output.append("V")
            else:
                output.append("IX")

        #sort the tens place
        if i == 1:
            if int(reverse[i]) < 4:
                output.append("X"*int(reverse[i]))
            elif int(reverse[i]) == 4:
                output.append("XL")
            elif int(reverse[i]) == 5:
                output.append("L")
            elif int(reverse[i]) < 9 and int(reverse[i]) > 5:
                output.append("X"*(int(reverse[i])-5))
                output.append("L")
            else: 
                output.append("XC")

        #sort the hundreds place
        if i == 2:    
            if int(reverse[i]) < 4:
                output.append("C"*int(reverse[i]))
            elif int(reverse[i]) == 4:
                output.append("CD")
            elif int(reverse[i]) == 5:
                output.append("D")
            elif int(reverse[i]) < 9 and int(reverse[i]) > 5:
                output.append("C"*(int(reverse[i])-5))
                output.append("D")
            else: 
                output.append("CM")
        
        #sort thousandths place
        if i == 3:    
            output.append("M"*int(reverse[i]))

    #reverse the output again to correct the order
    output.reverse()
    #print the output with all numbers joined, without spaces
    print(''.join(output))

arab_to_rom(4567)
