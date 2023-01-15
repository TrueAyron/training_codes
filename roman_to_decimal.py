def roman_to_decimal(rom):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec_val = 0
    for i in range(len(rom)):
        if i > 0 and rom_val[rom[i]] > rom_val[rom[i - 1]]:
            dec_val += rom_val[rom[i]] - 2 * rom_val[rom[i - 1]]
        else:
            dec_val += rom_val[rom[i]]
    return dec_val

def decimal_to_roman(dec):
    dec_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_val = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    while dec > 0:
        for _ in range(dec // dec_val[i]):
            roman_num += rom_val[i]
            dec -= dec_val[i]
        i += 1
    return roman_num

print(decimal_to_roman(14)) # output XIV
print(decimal_to_roman(21)) # output XXI


print(roman_to_decimal("XIV")) # output 14
print(roman_to_decimal("XXI")) # output 21
