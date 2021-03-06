from PIL import Image
import glob
import os
from config import TEMP_FILES, GRAPHS_FILES, PNG_STORAGE


def check_directories():
    """Функция проверки директорий, необходимых для работы программы

    Если какая-то из директорий отсутствует, создает ее
    """
    if not os.path.exists(TEMP_FILES):
        os.mkdir(TEMP_FILES)
    if not os.path.exists(GRAPHS_FILES):
        os.mkdir(GRAPHS_FILES)


def make_gif():
    """Функция создания gif из исходных png картинок графов"""
    check_directories()
    frames = []
    imgs = sorted(glob.glob(PNG_STORAGE))
    if len(imgs):
        for i in imgs:
            new_frame = Image.open(i)
            frames.append(new_frame)

        frames[0].save(f'{TEMP_FILES}/animated_graph.gif', format='GIF',
                       append_images=frames[1:],
                       save_all=True,
                       duration=300, loop=0)


def graph_deleting():
    """Функция для очистки директории с графами"""
    check_directories()
    imgs = glob.glob(PNG_STORAGE)
    for img in imgs:
        if os.path.exists(img):
          os.remove(img)
