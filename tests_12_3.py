import suite_12_3 as st
import unittest


tests = unittest.TestSuite()

tests.addTest(unittest.TestLoader().loadTestsFromTestCase(st.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(st.TournamentTest))

tests_run = unittest.TextTestRunner(verbosity=2)
tests_run.run(tests)


