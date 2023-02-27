class Employee:
    '''
    Simple employee class for testing
    '''
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return f'{self.first}.{self.last}@testemail.com'
    
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    
    @property
    def salary_after_tax(self):
        return self.salary*0.8
    
