import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_FILES = f"{ROOT_DIR}/tmp"
GRAPHS_FILES = f"{TEMP_FILES}/graphs"
PNG_STORAGE = f"{GRAPHS_FILES}/*.png"
