import unittest
from jasper import topStories



class JasperTestCase(unittest.TestCase):
    def test_topStories(self):
        self.assertTrue(topStories())


if __name__ == '__main__':
    unittest.main()
