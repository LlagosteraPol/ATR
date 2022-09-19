from setuptools import setup

setup(
    name='atr',
    version='1.0.0',
    author='Pol Llagostera Blasco',
    author_email='llagosterapol.work@gmail.com',
    packages=['atr', 'atr.relmodules'],
    url='https://github.com/LlagosteraPol/ATR',
    license='LICENSE.txt',
    description='This library provides a tool to calculate the all-terminal reliability polynomial of any undirected graph.',
    long_description='README.rst',
    long_description_content_type='text/markdown',
    install_requires=[
           "networkx >= 2.5.1",
           "sympy >= 1.4.0",
           "numpy >= 1.21.6"
       ],
)
