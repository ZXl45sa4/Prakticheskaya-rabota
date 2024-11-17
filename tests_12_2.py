import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = rat.Runner('Усейн', 10)
        self.Andrey = rat.Runner('Андрей', 9)
        self.Nick = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_Usain_and_Nick(self):
        tournament = rat.Tournament(90, self.Usain, self.Nick)
        result = tournament.start()
        # сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_Usain_and_nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_Andrey_and_Nick(self):
        tournament = rat.Tournament(90, self.Andrey, self.Nick)
        result = tournament.start()
        # сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_Andrey_and_Nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_Usain_Andrey_and_Nick(self):
        tournament = rat.Tournament(90, self.Usain, self.Andrey, self.Nick)
        result = tournament.start()
        # сохраняем имена бегунов
        formatted_result = {place: runner.name for place, runner in result.items()}
        TournamentTest.all_results['test_Usain_Andrey_and_Nick'] = formatted_result
        self.assertTrue(result[max(result.keys())].name == "Ник")


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
