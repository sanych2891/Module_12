import unittest
import test_module_12_4 as test
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                            format="%(asctime)s | %(levelname)s | %(message)s | %(name)s")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self, name='Alex'):
        try:
            name = test.Runner(name, speed=-1)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                name.walk()
            self.assertEqual(name.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self, name='Mike'):
        try:
            name = test.Runner(True)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                name.run()
            self.assertEqual(name.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self, name='Alex',name_ = 'Mike'):
        name = test.Runner(name)
        name_ = test.Runner(name_)
        for i in range(10):
            name.walk()
            name_.run()
        self.assertNotEqual(name.distance, name_.distance)


if __name__ == '__main__':
    unittest.main()

