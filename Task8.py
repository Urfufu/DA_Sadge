import unittest

import Task5 as prog
class  Task8(unittest.TestCase):
    def test_EngineType(self):
        TASK5 = prog.Task5
        self.assertEqual(TASK5.web, 'http://192.168.50.58/algenius')


if __name__ == '__main__':
    unittest.main()