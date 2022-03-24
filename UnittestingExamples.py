import unittest

def add(x,y):
    return x+y

def checkDivisibleby7(x):

    if x%7 == 0:
        return True
    else:
        return False

def cubevol(x):
    return x*x*x



class CheckVolume(unittest.TestCase):
    def test_volume_cube(self):
        x = 5.555
        result = cubevol(x)
        self.assertAlmostEqual(result,x*x*x)




class CheckDivisibleby(unittest.TestCase):
    def test_case_divisible(self):
        x = 14
        result = checkDivisibleby7(x)
        self.assertTrue(result)


    def test_case_divisible1(self):
        x =9
        result = checkDivisibleby7(x)
        self.assertFalse(result)



class myApp2(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 22
        result = add(a,b)
        self.assertEqual(a+b,result)

    def test_case2(self):
        a = 12.5
        b = 12.9
        result = add(a,b)
        self.assertEqual(25.4,result)


if __name__ == "__main__":
    unittest.main()
