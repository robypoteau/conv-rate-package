from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    author="Roby Poteau"
    ,author_email="robypoteau@gmail.com"
    ,name="convrate"
    ,version='1.0'
    ,long_description=README
    ,url='https://github.com/robypoteau/conv-rate-package'
    ,packages=find_packages()
    ,license='MIT'
    ,setup_requires=['pytest-runner']
    ,tests_require=['pytest']
 )
