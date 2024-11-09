import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj_1 = runner.Runner('Объект_1')
        for _ in range(10):
            obj_1.walk()
        self.assertEqual(obj_1.distance, 50)

    def test_run(self):
        obj_2 = runner.Runner('Объект_2')
        for _ in range(10):
            obj_2.run()
        self.assertEqual(obj_2.distance, 50)

    def test_challenge(self):
        obj_3 = runner.Runner('Объект_3')
        obj_4 = runner.Runner('Объект_4')
        for _ in range(10):
            obj_3.walk()
            obj_4.run()
        self.assertEqual(obj_3.distance, obj_4.distance)


if __name__ == "__main__":
    unittest.main()

