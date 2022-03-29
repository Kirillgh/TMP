import unittest
import tasks.task_19_dec as task_19_dec


test_data = [
    {
        'preufer_code': [1, 1, 5, 5, 2, 6, 5],
        'node_array': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'output': [(1, 3), (1, 4), (5, 1), (5, 7), (2, 8), (6, 2), (5, 6), (5, 9)]
    },
    {
        'preufer_code': [4, 4, 4, 5],
        'node_array': [1, 2, 3, 4, 5, 6],
        'output': [(4, 1), (4, 2), (4, 3), (5, 4), (5, 6)]
    },
    {
        'preufer_code': [1, 5, 2, 6, 6, 2, 1, 3],
        'node_array': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'output': [(1, 4), (5, 7), (2, 5), (6, 8), (6, 9), (2, 6), (1, 2), (3, 1), (3, 10)]
    },
    {
        'preufer_code': [1, 2, 2, 1, 1],
        'node_array': [1, 2, 3, 4, 5, 6, 7],
        'output': [(1, 3), (2, 4), (2, 5), (1, 2), (1, 6), (1, 7)]
    },
    {
        'preufer_code': [1, 4, 5, 5],
        'node_array': [1, 2, 3, 4, 5, 6],
        'output': [(1, 2), (4, 1), (5, 3), (5, 4), (5, 6)]
    }
]


class TestTask19Dec(unittest.TestCase):

    def test_dec(self):
        for data in test_data:
            graph, pos = task_19_dec.preprocessing(data['node_array'])
            result = task_19_dec.computing(graph, pos, data['preufer_code'], data['node_array'])
            self.assertEqual(result, data['output'])


if __name__ == '__main__':
    unittest.main()
