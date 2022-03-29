import unittest
import tasks.task_16 as task_16


test_data = [
    {
        'node_array': [1, 2, 3, 4, 5, 6, 7],
        'edges': [(1, 2, 5), (1, 3, 7), (1, 4, 9), (2, 3, 1), (2, 5, 4), (3, 6, 4), (4, 6, 1), (4, 7, 1), (5, 6, 4), (5, 7, 2), (6, 7, 6)],
        'min_edge_cut': {(4, 7), (5, 7), (6, 7)},
        'max_flow': 9
    }
]


class TestTask16(unittest.TestCase):

    def test_enc(self):
        for data in test_data:
            min_edge_cut, max_flow = task_16.processing(data['node_array'], data['edges'])
            self.assertEqual(min_edge_cut, data['min_edge_cut'])
            self.assertEqual(max_flow, data['max_flow'])


if __name__ == '__main__':
    unittest.main()