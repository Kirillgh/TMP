import networkx
import matplotlib.pyplot as plt
from project_utils import video_maker


def number_of_pic(num):
    """Функция для форматирования нумерации картинок

       Parameters
       ----------
       num : int
           Номер картинки.

       Example
       -------
           >>> number_of_pic(1)
           "01"
           >>> number_of_pic(10)
           "10"

       Returns
       -------
       str
           Форматированный номер.
       """
    if num < 10:
        return f'0{num}'
    return f'{num}'


def draw(graph, pos, result, i):
    """Функция для отрисовки и сохранения графа

        Parameters
        ----------
        graph : Graph
            Граф.
        pos : dict
            Словарь позиций вершин графа.
        result : list
            Список связей в графе.
        i : int
            Номер картинки.
        """
    networkx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_color='g', node_size=500)
    networkx.draw_networkx_labels(graph, pos)
    networkx.draw_networkx_edges(graph, pos, edgelist=result)
    plt.savefig(f'../tmp/graphs/{number_of_pic(i+1)}.png')


def find_pair(preufer_code, node_array):
    """Функция для создания пар связей вершин

       Parameters
       ----------
       preufer_code : list
           Код прюфера.
       node_array : list
           Список вершин.

       Example
       -------
           >>> find_pair([1, 5, 2, 6, 6, 2, 1, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
           (1, 4, [5, 2, 6, 6, 2, 1, 3], [2, 3, 4, 5, 6, 7, 8, 9, 10])

       Returns
       -------
       tuple
           Первое значение кода прюфера, минимальная вершина (не содержащаяся в нем),
           код прюфера без этого значения, вершина без этого значения.
    """
    for i in node_array:
        if i not in preufer_code:
            node_array.remove(i)
            return preufer_code[0], i, preufer_code[1:], node_array
    raise Exception


def preprocessing(node_array):
    """Функция создания графа

         Parameters
         ----------
         node_array : list
             Список вершин.

         Returns
         -------
         tuple
             Граф, словарь вершин.
    """
    video_maker.graph_deleting()
    graph = networkx.Graph()
    graph.add_nodes_from(node_array)
    pos = networkx.spring_layout(graph)
    return graph, pos


def input_values():
    """Функция ввода значений

         Returns
         -------
         tuple
             Код прюфера, список вершин.
    """
    string = input('Введите код Прюфера: ')
    preufer_code = list(map(int, string.split()))
    node_array = list(range(1, len(preufer_code)+3))
    return preufer_code, node_array


def computing(graph, pos, preufer_code, node_array):
    """Функция обработки графа

         Parameters
         ----------
         graph : Graph
             Граф.
         pos : dict
             Словарь позиций вершин графа.
         preufer_code : list
             Код прюфера.
         node_array : list
             Список вершин.
    """
    result = []
    for i in range(len(preufer_code)):
        first_elem, second_elem, preufer_code, node_array = find_pair(preufer_code, node_array)
        result.append((first_elem, second_elem))
        draw(graph, pos, result, i)
    result.append(tuple(node_array))
    draw(graph, pos, result, i + 1)
    print(result)
    video_maker.make_gif()


def main():
    """Основная функция модуля, решающего задачу №19 Декодер Прюфера

    Считывает с консоли код Прюфера, создает список вершин и восстанавливает исходный граф.
    """
    preufer_code, node_array = input_values()
    graph, pos = preprocessing(node_array)
    computing(graph, pos, preufer_code, node_array)

