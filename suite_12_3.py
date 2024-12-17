import unittest
import mod_12_exp_2 as mex


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self, name='Alex'):
        name = mex.Runner(name)
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self, name='Mike'):
        name = mex.Runner(name)
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self, name='Alex',name_ = 'Mike'):
        name = mex.Runner(name)
        name_ = mex.Runner(name_)
        for i in range(10):
            name.walk()
            name_.run()
        self.assertNotEqual(name.distance, name_.distance)


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self, num=1):
        tournament = mex.Tournament(90, self.ran_u, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.ran_n.name)
        self.all_results[num] = all_results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self, num=2):
        tournament = mex.Tournament(90, self.ran_a, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.ran_n.name)
        self.all_results[num] = all_results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self, num=3):
        tournament = mex.Tournament(90, self.ran_u, self.ran_a, self.ran_n)
        all_results = tournament.start()
        self.assertTrue(all_results[3], self.ran_n.name)
        self.all_results[num] = all_results


if __name__ == '__main__':
    unittest.main()


