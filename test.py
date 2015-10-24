from dragon import Dragon
import unittest

class test(unittest.TestCase):
    def testCreateDragon(self):
        dragon = Dragon("Razil", 20, 30)
        self.failUnlessEqual("Razil", dragon.getName())

    def testIncreaseStrength(self):
        dragon = Dragon("Razil", 20, 30)
        dragon.setStrength(20)
        self.failUnlessEqual(40, dragon.getStrength())

    def testFail(self):
        dragon = Dragon("Razil", 20, 30)
        dragon.setDefence(20)
        self.failUnlessEqual(30, dragon.getStrength())

if __name__ == '__main__':
    unittest.main()
