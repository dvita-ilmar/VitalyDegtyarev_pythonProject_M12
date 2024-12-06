"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №12.3
Домашнее задание по теме "Систематизация и пропуск тестов".
"""


import unittest
from module_12_1 import RunnerTest
from module_12_2 import TournamentTest


UniSportTests = unittest.TestSuite()
UniSportTests.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
UniSportTests.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(UniSportTests)