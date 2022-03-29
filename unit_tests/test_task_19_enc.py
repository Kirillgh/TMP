import unittest
import tasks.task_19_enc as task_19_enc


test_data = [
    {
        'node_array': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'edges': [(1, 2), (1, 7), (1, 8), (2, 6), (3, 5), (4, 5), (5, 6), (5, 9)],
        'preufer_code': [5, 5, 1, 1, 2, 6, 5],
        'last_edge': [(5, 9)]
    }
]


class TestTask19Enc(unittest.TestCase):

    def test_enc(self):
        for data in test_data:
            graph, number_of_picture = task_19_enc.preprocessing(data['node_array'], data['edges'])
            e, res = task_19_enc.computing(data['edges'], number_of_picture, graph)
            self.assertEqual(e, data['last_edge'])
            self.assertEqual(res, data['preufer_code'])


if __name__ == '__main__':
    unittest.main()