def roman_to_decimal(rom):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec_val = 0
    for i in range(len(rom)):
        if i > 0 and rom_val[rom[i]] > rom_val[rom[i - 1]]:
            dec_val += rom_val[rom[i]] - 2 * rom_val[rom[i - 1]]
        else:
            dec_val += rom_val[rom[i]]
    return dec_val

print(roman_to_decimal("XIV")) # output 14
print(roman_to_decimal("XXI")) # output 21
