file = open("data.txt", "r")
passports = [[]]

for line in file:
    if line != '\n':
        #Add details to current passport
        passports[len(passports) - 1].extend(line.split(' '))    
    else:
        #Start a new passport
        passports.append([])
        
passports = [[credential.split(':')[0] for credential in passport] for passport in passports]

def valid_passport(passport):
    return sorted(passport) == sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

def valid_np_cred(passport):
    return sorted(passport) == sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    
print(sum([valid_passport(p) or valid_np_cred(p) for p in passports ]))    