import app
import unittest

class TestPassports(unittest.TestCase):

    def test_byr_valid(self):
        self.assertTrue(app.valid_byr(['byr:2002']))

    def test_byr_invalid(self):
        self.assertFalse(app.valid_byr(['byr:2003']))

    def test_hgt_valid_in(self):
        self.assertTrue(app.valid_hgt(['hgt:60in']))

    def test_hgt_valid_cm(self):
        self.assertTrue(app.valid_hgt(['hgt:190cm']))
    
    def test_hgt_invalid_in(self):
        self.assertFalse(app.valid_hgt(['hgt:190in']))
    
    def test_hgt_invalid_none(self):
        self.assertFalse(app.valid_hgt(['hgt:190']))

    def test_hcl_valid(self):
        self.assertTrue(app.valid_hcl(['hcl:#123abc']))
    
    def test_hcl_invalid(self): 
        self.assertFalse(app.valid_hcl(['hcl:#123abz']))
    
    def test_hcl_invalid_2(self): 
        self.assertFalse(app.valid_hcl(['hcl:123abc']))

    def test_ecl_valid(self):   
        self.assertTrue(app.valid_ecl(['ecl:brn']))
    
    def test_ecl_invalid(self): 
        self.assertFalse(app.valid_ecl(['ecl:wat']))

    def test_pid_valid(self):   
        self.assertTrue(app.valid_pid(['pid:000000001']))
    
    def test_pid_invalid(self): 
        self.assertFalse(app.valid_pid(['pid:0123456789']))
        
    def test_invalid_1(self):
        self.assertFalse(app.all_creds_valid('eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'.split(' ')))        
   
    def test_invalid_2(self):
        self.assertFalse(app.all_creds_valid('iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946'.split(' ')))

    def test_invalid_3(self):
        self.assertFalse(app.all_creds_valid('hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277'.split(' ')))

    def test_invalid_4(self):
        self.assertFalse(app.all_creds_valid('hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'.split(' ')))     
        
    def test_valid_1(self):
        self.assertTrue(app.all_creds_valid('pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'.split(' ')))        
   
    def test_valid_2(self):
        self.assertTrue(app.all_creds_valid('eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm'.split(' ')))

    def test_valid_3(self):
        self.assertTrue(app.all_creds_valid('hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022'.split(' ')))

    def test_valid_4(self):
        self.assertTrue(app.all_creds_valid('iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'.split(' ')))  
    
if __name__ == '__main__':
    unittest.main()

