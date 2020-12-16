class TicketRule():
    
    def __init__(self, field, bounds):
        self.field = field
        self.bounds = bounds
    
    def __str__(self):
        return self.field + ': ' + ','.join(str(x) for x in self.valid_nums)
        
    @property
    def valid_nums(self):
        valid_nums = []
        for rnge in self.bounds:
            lower, upper = [int(x) for x in rnge.split('-')]
            for i in range(lower, upper + 1):
                valid_nums.append(i)
        return valid_nums
    
    def validate_value(self, num):
        return num in self.valid_nums                