"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №12.2
Домашнее задание по теме "Методы Юнит-тестирования"
"""


import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results.append(tournament1.start())
        self.assertTrue(TournamentTest.all_results[0][2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results.append(tournament2.start())
        self.assertTrue(TournamentTest.all_results[1][2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append(tournament3.start())
        self.assertTrue(TournamentTest.all_results[2][3], 'Ник')

    @classmethod
    def tearDownClass(cls):
        for tournament in TournamentTest.all_results:
            for key, value in tournament.items():
                print(f'{key}:{value}  ', end="")
            print('\n')


if __name__ == '__main__':
    unittest.main()