def roman_converter(num):
    if not isinstance(num, int):
        return None
    
    if num <= 0 or num >= 4000:
        return None
    
    ROMAN_NUMS = [
        (50, "L"), (10,"X"),(5, "V"),(1, "I")
    ]

    out = ''

    for values, sym in ROMAN_NUMS:
        cnt=0
        while num >= values:
            if cnt < 3:
                cnt+=1
                out+=sym
                num-=values
            else:
                x=2
                x-=1
                sym = sym.replace('I', 'IV').replace('V', 'IX')
                out += sym
                num -= values - 1

    return out

print(roman_converter(58))  # Should return "LVIII"
print(roman_converter(4))   # Should return "IV"