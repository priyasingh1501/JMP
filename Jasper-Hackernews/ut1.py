import unittest
from jasper import latestStories

class JasperTestCase(unittest.TestCase):
    def test_latestStories(self):
        self.assertTrue(latestStories())
if __name__ == '__main__':
    unittest.main()
