import unittest
from pairs import multiply_pair_components, multiply_triples_components

class Day1Test(unittest.TestCase):
  def test_find_1721_299(self):
    input = [1721,979,366,299,675,1456]
    self.assertEqual(514579, multiply_pair_components(input))
  def test_find_2000_20(self):
    input = [455, 789, 20, 2000, 1189]
    self.assertEqual(40000, multiply_pair_components(input))
  def test_find_979_675_366(self):
    input = [1721,979,366,299,675,1456]
    self.assertEqual(241861950, multiply_triples_components(input))


if __name__ == '__main__':
  unittest.main()
