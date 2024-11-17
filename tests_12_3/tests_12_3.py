import unittest


class RunnerTest(unittest.TestCase):
    if_frozen = False

    @unittest.skipIf(if_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        pass

    @unittest.skipIf(if_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        pass

    @unittest.skipIf(if_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        pass


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        pass

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        pass

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        pass
