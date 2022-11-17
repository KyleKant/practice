import unittest
import thi


class UserValidationTests(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.email = 'thi@thi.com'
    #     self.password = 'ONhaNam0941@'
    # return super().setUp()

    def test_user_valid(self):
        email = 'thi@thi.com'
        password = 'ONhaNam0941@'
        result = thi.user_validate(email, password)
        self.assertEqual(result, 'User Valid')

    def test_email_invalid(self):
        email = 'thithi.com'
        password = 'ONhaNam0941@'
        result = thi.user_validate(email, password)
        self.assertEqual(result, 'Email Invalid')

    def test_password_invalid(self):
        email = 'thi@thi.com'
        password = '1234'
        result = thi.user_validate(email, password)
        self.assertEqual(result, 'Password Invalid')

    def test_user_invalid(self):
        email = 'thi@hi'
        password = 'sadfjwerasdfa'
        result = thi.user_validate(email, password)
        self.assertEqual(result, 'User Invalid')


class GuessNumberTests(unittest.TestCase):
    def test_get_random_number(self):
        first = 1
        last = 2
        result = thi.get_random_number(first, last)
        self.assertIsInstance(result, int)

    def test_get_number_entered(self):
        result = thi.get_number_entered(1, 2)
        self.assertIsInstance(result, int)

    def test_check_guess(self):
        result = thi.check_guess(5, 5, 1, 10)
        self.assertTrue(result)

    def test_check_guess_wrong(self):
        result = thi.check_guess(3, 5, 1, 10)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = thi.check_guess(14, 5, 1, 10)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = thi.check_guess('3', 5, 1, 10)
        self.assertFalse(result)


class ConvertToPngImagesTests(unittest.TestCase):
    def test_dir_exist(self):
        dir = '.\images\\'
        result = thi.isDirExist(dir)
        self.assertTrue(result)

    def test_dir_not_exist(self):
        dir = '.\\name\\'
        result = thi.isDirExist(dir)
        self.assertFalse(result)
    pass


if __name__ == '__main__':
    unittest.main()
