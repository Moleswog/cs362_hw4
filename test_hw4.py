import unittest
import hw4

class HW4Test(unittest.TestCase):
    def test_q1(self):
        # test on positive input
        result = hw4.cubeVolume(2)
        self.assertEqual(result, 8)
        
        # test on negative input
        result = hw4.cubeVolume(-.5)
        self.assertEqual(result, -.125)
        
        # test on string input
        result = hw4.cubeVolume("")
        self.assertRaises(TypeError)

    def test_q2(self):

        # test on mixed input
        result = hw4.avgList([-2,-1, 0 , 1, 3])
        self.assertEqual(result, .2)
        
        # test on empty list
        result = hw4.avgList([])
        self.assertIsNone(result)

        # test on string input
        result = hw4.avgList([1,"2",3])
        self.assertRaises(TypeError)

    def test_q3(self):
        # test on string input
        result = hw4.nameGen("firstname", "lastname")
        self.assertEqual(result, "firstname lastname")

        # test on int input
        result = hw4.nameGen(0, 1)
        self.assertRaises(TypeError)

        # test on empty input
        result = hw4.nameGen("", "")
        self.assertEqual(result, " ")



if __name__ == "__main__":
    unittest.main()
