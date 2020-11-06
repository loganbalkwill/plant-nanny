from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='Plant-Nanny',
    version='0.1.0',
    description='Automate and monitor plant-care tasks',
    long_description=readme,
    author='Logan Balkwill',
    author_email='lgb0020@gmail.com',
    url='https://github.com/loganbalkwill/plant-nanny',
    license=license,
    packages=find_packages(exclude=('tests', 'sensors'))
)