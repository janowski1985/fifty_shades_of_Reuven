def hex_output(number):

# assumption: number == 0xnumber

    count = 0
    
    for power, digit in enumerate(reversed(number)):
        print(f'{power} : {digit}')
        
# in int second value is base = this means that we put hex value like 0xA0

        count += int(digit, 16) * 16**power
    
    return count
