import unittest
import mod_12_exp_Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self, name='Alex'):
        name = mod_12_exp_Runner.Runner(name)
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self, name='Mike'):
        name = mod_12_exp_Runner.Runner(name)
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self, name='Alex',name_ = 'Mike'):
        name = mod_12_exp_Runner.Runner(name)
        name_ = mod_12_exp_Runner.Runner(name_)
        for i in range(10):
            name.walk()
            name_.run()
        self.assertNotEqual(name.distance, name_.distance)


if __name__ == '__main__':
    unittest.main()

