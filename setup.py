from setuptools import setup
import os


current_folder = os.path.dirname(os.path.realpath(__file__))
requirementPath = current_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name='TMP',
    version='1.0',
    install_requires=install_requires,
    url='https://github.com/Kirillgh/TMP',
    license='MIT',
    author='mistone',
    author_email='kutuzovslava1@gmail.com',
    description='Technologies and methods of programming',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'TMP = TMP:main',
        ],
    }
)
