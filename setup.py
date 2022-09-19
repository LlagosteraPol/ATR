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
    long_description=open('README.rst').read(),
    install_requires=[
           "networkx >= 2.5.1",
           "sympy >= 1.4.0",
           "numpy >= 1.21.6"
       ],
)
