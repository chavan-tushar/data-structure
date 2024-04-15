def romanToInt(s: str) -> int:
        symbol_and_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        intToReturn = 0
        is_special = False

        for pos, char in enumerate(s):
            if is_special == True:
                is_special = False
                continue
    
            if char == "I" and s[pos:pos+2] == "IV":
                intToReturn += symbol_and_values["IV"]
                is_special = True
                continue

            if char == "I" and s[pos:pos+2] == "IX":
                intToReturn += symbol_and_values["IX"]
                is_special = True
                continue
            if char == "X" and s[pos:pos+2] == "XL":
                intToReturn += symbol_and_values["XL"]
                is_special = True
                continue
            if char == "X" and s[pos:pos+2] == "XC":
                intToReturn += symbol_and_values["XC"]
                is_special = True
                continue
            if char == "C" and s[pos:pos+2] == "CD":
                intToReturn += symbol_and_values["CD"]
                is_special = True
                continue
            if char == "C" and s[pos:pos+2] == "CM":
                intToReturn += symbol_and_values["CM"]
                is_special = True
                continue
            
            intToReturn += symbol_and_values[char]
            is_special = False

        return intToReturn

print(romanToInt("MCMXCIV"))