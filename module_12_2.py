import mod_12_exp_2 as mex
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.ran_u = mex.Runner('Усэйн', 10)
        self.ran_a = mex.Runner('Андрей', 9)
        self.ran_n = mex.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print(f'test: {i}')
            for key, value in j.items():
                print(f'\t{key}: {value.name}')

    def test_1(self, num=1):
        tournament = mex.Tournament(90, self.ran_u, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.ran_n.name)
        self.all_results[num] = all_results


    def test_2(self, num=2):
        tournament = mex.Tournament(90, self.ran_a, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.ran_n.name)
        self.all_results[num] = all_results


    def test_3(self, num=3):
        tournament = mex.Tournament(90, self.ran_u, self.ran_a, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[3], self.ran_n.name)
        self.all_results[num] = all_results


if __name__ == '__main__':
    unittest.main()
