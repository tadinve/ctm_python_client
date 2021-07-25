from setuptools import find_packages, setup

setup(
    name='naga',
    packages=find_packages(),
    version='0.1.0',
    description='Python Workflows for Control-M',
    author='Venkatesh Tadinada @ BMC Innovations Lab',
    license='Apache 2.0',
    install_requires=[
          'graphviz', 'requests==2.23.0',
    ],
)