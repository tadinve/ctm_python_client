from setuptools import find_packages, setup

setup(
    name='ctm_python_client',
    packages=find_packages(),
    version='0.3.0',
    description='Python Workflows for Control-M',
    author='Venkatesh Tadinada @ BMC Innovations Lab',
    license='Apache 2.0',
    install_requires=['graphviz>=0.10', 
                        'requests>=2.23.0',
                        'urllib3'],
)