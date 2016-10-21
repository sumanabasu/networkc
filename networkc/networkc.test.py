import unittest
import  imp
networkc = imp.load_source('networkc', 'networkc/networkc.py')

class networkcTest(unittest.TestCase):
    def test_calcCentrality(self):
        G = networkc.readGraph('networkc/test.csv')
        dcD, dcC, dcB = networkc.calcCentrality(G, True, True, True)
        dcD = dcD.values.tolist()
        dcC = dcC.values.tolist()
        dcB = dcB.values.tolist()
        dcD_real = [['1', 1.0], ['2', 0.5], ['0', 0.5], ['11', 0.25], ['4', 0.25]]
        dcC_real = [['1', 1.0], ['2', 0.6666666666666666], ['0', 0.6666666666666666], ['11', 0.5714285714285714], ['4', 0.5714285714285714]]
        dcB_real = [['1', 0.8333333333333333], ['11', 0.0], ['4', 0.0], ['2', 0.0], ['0', 0.0]]
        print dcB
        self.assertEqual(dcD, dcD_real)
        self.assertEqual(dcC, dcC_real)
        self.assertEqual(dcB, dcB_real)

if __name__ == "__main__":
    unittest.main()