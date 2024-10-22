import unittest

from personnage import Personnage


class PersonnageTest(unittest.TestCase):
    def test_dix_hp_origine(self):
        personnage = Personnage()
        self.assertEqual(10, personnage.get_points_de_vie())


if __name__ == '__main__':
    unittest.main()
