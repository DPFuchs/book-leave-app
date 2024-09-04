import unittest, app

class TestLogin(unittest.TestCase):
    def test_Valid_Login(self):
        self.assertTrue(app.login("Dylan", "SonGoku2001", ["Dylan","John", "Ser"], ["SonGoku2001", "ABCD1234", "QWER!@#$"]))        
    
    def test_InvalidLogin(self):
        self.assertFalse(app.login("dyas", "dsjklas!@#$", ["Dylan","John", "Ser"], ["SonGoku2001", "ABCD1234", "QWER!@#$"]))
    
    def test_ValidUsernameInvalidPassword(self):
        self.assertFalse(app.login("Dylan", "asd1234", ["Dylan","John", "Ser"], ["SonGoku2001", "ABCD1234", "QWER!@#$"]))
    
    def test_InvalidUsernameValidPassword(self):
        self.assertFalse(app.login("Ser", "SonGoku2001", ["Dylan","John", "Ser"], ["SonGoku2001", "ABCD1234", "QWER!@#$"]))
    
    def test_captcha(self):
        self.assertFalse(app.Captcha().isnumeric())

    def test_BookChoiceEqualValues(self):
        self.assertEqual(app.bookLeave(0,[10,20,30], 10), 0)
    
    def test_BookChoiceBiggerDaysBooked(self):
        self.assertEqual(app.bookLeave(1,[10,20,30], 30), 20)
    
    def test_BookChoiceSmallerDaysBooked(self):
        self.assertEqual(app.bookLeave(1,[10,20,30], 5), 15)

if __name__ == '__main__':
    unittest.main()