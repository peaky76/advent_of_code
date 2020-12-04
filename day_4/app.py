file = open("data.txt", "r")
passports = [[]]

for line in file:
    if line != '\n':
        #Add details to current passport
        passports[len(passports) - 1].extend(line.split(' '))    
    else:
        #Start a new passport
        passports.append([])

def get_keys(passport):        
    return [credential.split(':')[0] for credential in passport]

def valid_passport(passport):
    return sorted(get_keys(passport)) == sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

def valid_np_cred(passport):
    return sorted(get_keys(passport)) == sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        
print(sum([valid_passport(p) or valid_np_cred(p) for p in passports ]))    


#VALIDATION RULES

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.