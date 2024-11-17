import unittest
import tests_12_3

ST = unittest.TestSuite()
ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

Un = unittest.TextTestRunner(verbosity=2)
Un.run(ST)
