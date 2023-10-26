from setuptools import setup, find_namespace_packages

setup(
    name='pythonProject6',
    version='0.1.0',
    description='Very useful code',
    author='lapko Artem',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_vvm.main:greeting']}
)