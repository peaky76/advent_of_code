import re

file = open("data.txt", "r")
passports = [[]]

for line in file:
    line = line.rstrip('\n')
    if line:
        #Add details to current passport
        passports[len(passports) - 1].extend(line.split(' '))    
    else:
        #Start a new passport
        passports.append([])

# PART ONE
def get_details(passport):        
    return dict([credential.split(':') for credential in passport])

def valid_passport(passport):
    return all(key in get_details(passport).keys() for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

def valid_np_cred(passport):
    return all(key in get_details(passport).keys() for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

print(sum([valid_passport(p) or valid_np_cred(p) for p in passports]))    

#PART TWO
def valid_byr(passport):
    return 1920 <= int(get_details(passport)['byr']) <= 2002

def valid_iyr(passport):
    return 2010 <= int(get_details(passport)['iyr']) <= 2020

def valid_eyr(passport):
    return 2020 <= int(get_details(passport)['eyr']) <= 2030

def valid_hgt(passport):
    hgt = get_details(passport)['hgt']
    if re.match(r'\d+',hgt):
        if re.search(r'cm', hgt):
            return hgt[:-2].isnumeric() and 150 <= int(hgt[:-2]) <= 193
        if re.search(r'in', hgt):
            return hgt[:-2].isnumeric() and 59 <= int(hgt[:-2]) <= 76
    return False

def valid_hcl(passport):
    return bool(re.match(r'#[0-9a-f]{6}', get_details(passport)['hcl'])) 

def valid_ecl(passport):
    return get_details(passport)['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(passport):
    pid = get_details(passport)['pid']
    return bool(re.fullmatch(r'[0-9]{9}', pid))    
        
def all_creds_valid(passport):
    funcs = [valid_byr, valid_iyr, valid_eyr, valid_hgt, valid_hcl, valid_ecl, valid_pid]
    return all([func(passport) for func in funcs])

print(sum([(valid_passport(p) or valid_np_cred(p)) and all_creds_valid(p) for p in passports]))  
