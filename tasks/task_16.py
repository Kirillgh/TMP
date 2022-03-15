import random
import networkx
from networkx.algorithms.connectivity import minimum_edge_cut
from networkx import maximum_flow_value
import matplotlib.pyplot as plt
from project_utils import video_maker


def random_edges(nodes):
    """Функция для генерации случайных связей с весами между вершинами графа

    Parameters
    ----------
    nodes : list
        Список вершин.

    Example
    -------
        >>> random_edges([0, 1, 2, 3])
        [(0, 1, 2.0), (0, 2, 1.0), (1, 2, 3.0), (2, 3, 2.0)]

    Returns
    -------
    list
        Список связей с весами.
    """
    edges_dict = dict()
    edges_list = []
    for i in range(len(nodes)):
        edges_dict[i] = []
        for j in range(i, len(nodes)):
            if i != j:
                edges_dict[i].append((i, j, random.randint(0, len(nodes))))
    if len(nodes) > 2:
        for i in edges_dict.keys():
            for j in random.choices(edges_dict[i], k=len(edges_dict[i])-len(edges_dict[i])//2):
                edges_list.append(j)
    return edges_list


def draw_and_save(graph, pos, edges):
    """Функция для отрисовки и сохранения графа

    Parameters
    ----------
    graph : DiGraph
        Граф.
    pos : dict
        Словарь позиций вершин графа.
    edges : list
        Список связей в графе.
    """
    video_maker.graph_deleting()
    networkx.draw_networkx_nodes(graph, pos, node_color='g', node_size=500)
    networkx.draw_networkx_labels(graph, pos)
    networkx.draw_networkx_edges(graph, pos, edgelist=edges)
    plt.savefig('./tmp/graphs/01.png')
    video_maker.make_gif()


def processing(nodes, edges):
    """Функция обработки графа

        Parameters
        ----------
        nodes : list
            Список вершин.
        edges : list
            Список связей между вершинами.

        Example
        -------
            >>> processing([0, 1, 2, 3], [(0, 1, 2.0), (0, 2, 1.0), (1, 2, 3.0), (2, 3, 2.0)])

        Returns
        -------
        tuple
            tuple, в котором первый элмент - минимальный разрез (dict) в формате: {(0, 6), (0, 2)};
             второй элемент - максимальный поток (int)
        """
    graph = networkx.DiGraph()
    graph.add_nodes_from(nodes)
    pos = networkx.circular_layout(graph)
    graph.add_weighted_edges_from(edges)

    draw_and_save(graph, pos, edges)

    return minimum_edge_cut(graph, nodes[0], nodes[-1]), maximum_flow_value(graph, nodes[0], nodes[-1], capacity='weight')


def main():
    """Основная функция модуля, решающего задачу №16

    Создает случайный граф, находит в нем максимальный поток и минимальный разрез,
    выводит ответ в консоль, сохраняет визуализированный граф в качестве картинки
    """
    nodes = list(range(random.randint(4, 12)))
    edges = random_edges(nodes)
    min_edge_cut, max_flow = processing(nodes, edges)
    print(f'Минимальный разрез: {min_edge_cut}\nМаксимальный поток: {max_flow}')
