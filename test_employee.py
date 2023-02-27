import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Tom', 'Smith', 50000)
        emp_2 = Employee('Peter','Jones', 100000)

        self.assertEqual(emp_1.email, 'Tom.Smith@testemail.com')
        self.assertEqual(emp_2.email, 'Peter.Jones@testemail.com')

        emp_1.first = "Jim"
        self.assertEqual(emp_1.email, 'Jim.Smith@testemail.com')

    def test_fullname(self):
        emp_1 = Employee('Tom', 'Smith', 50000)
        emp_2 = Employee('Peter','Jones', 100000)

        self.assertEqual(emp_1.full_name, 'Tom Smith')
        self.assertEqual(emp_2.full_name, 'Peter Jones')

if __name__ == "__main__":
    unittest.main()