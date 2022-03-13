from operator import itemgetter
import matplotlib.pyplot as plt
import networkx
#from project_utils import video_maker

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

####################################################################################
def input_values():
    """
    Функция ввода значений

    Returns
    -------
    tuple
        Список вершин графа, список ребер графа.
    """
    print("Введите значения вершин дерева в порядке возрастания через пробел")
    node_list = list(map(int, input().split()))

    print("Введите рёбра графа в следующем формате: 1 2, 2 3, 3 4")
    e = []
    try:
        temp = input().split(', ')
        for i in temp:
            tmp = tuple(map(int, i.split()))
            e.append(tmp)
        print("Ваше дерево ", e)
    except:
        print('Формат неверный! Введите по примеру: 1 2, 2 3, 3 4')
    return node_list, e
####################################################################################
def preprocessing(node_list, e):
    """Функция создания графа

            Parameters
            ----------
            node_list : list
                Список вершин.
            e : list
                Список ребер.
            Returns
            -------
            tuple
                Граф, номер картинки.
        """
    number_of_picture = 0

    video_maker.graph_deleting()
    graph = networkx.Graph()
    graph.add_nodes_from(node_list)
    pos = networkx.spring_layout(graph)
    networkx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_color='g', node_size=500)
    networkx.draw_networkx_labels(graph, pos)
    networkx.draw_networkx_edges(graph, pos, edgelist=e)
    plt.savefig(f'../tmp/graphs/{number_of_pic(number_of_picture)}.png')
    plt.clf()
    return graph, number_of_picture
####################################################################################
def computing(e, number_of_picture, graph):
    """Функция обработки графа
            Parameters
            ----------
            e : list
                Список ребер.
            number_of_picture : int
                Номер картинки.
            graph : Graph
                Граф.
        """
    res = []
    while len(e) > 1:
        number_of_picture += 1
        temp = dict()
        for i in e:
            for j in i:
                if j in temp:
                    temp[j] += 1
                else:
                    temp[j] = 1

        sorted_list = sorted(temp.items(), key=itemgetter(1))
        set_of_values = []
        for i in sorted_list:
            if i[1] == 1:
                set_of_values.append(i[0])
        new_sorted_list = sorted(set_of_values)

        for i in e:
            if new_sorted_list[0] in i:
                if new_sorted_list[0] == i[0]:
                    res.append(i[1])
                else:
                    res.append(i[0])
                e.remove(i)

        pos = networkx.spring_layout(graph)
        graph.remove_node(new_sorted_list[0])
        networkx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), node_color='g', node_size=500)
        networkx.draw_networkx_labels(graph, pos)
        networkx.draw_networkx_edges(graph, pos, edgelist=e)
        plt.savefig(f'../tmp/graphs/{number_of_pic(number_of_picture)}.png')
        plt.clf()

    video_maker.make_gif()
    print("Оставшееся ребро", e)
    print("Код Прюфера ", res)
    ####################################################################################

def main():
    """
    Основная функция модуля, решающего задачу №19 Кодер Прюфера

    Принимает на вход вершины графа в порядке возрастания, а также сам граф.
    Итоговый результат - оставшееся после выполнения алгоритма ребро и Код Прюфера.
    """
    node_list, e = input_values()
    graph, number_of_picture = preprocessing(node_list, e)
    computing(e, number_of_picture, graph)
