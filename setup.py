from setuptools import setup, find_packages

setup(name="convrate"
    ,version='1.0'
    ,packages=find_packages()
    ,license='MIT'
    ,setup_requires=['pytest-runner']
    ,tests_require=['pytest']
 )
