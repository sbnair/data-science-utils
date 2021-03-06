from setuptools import find_packages, setup

setup(name='data_science_utils',
      version='0.1.45',
      description='Utils for use in python with pandas and numpy',
      url='https://github.com/faizanahemad/data-science-utils',
      author='Faizan Ahemad',
      author_email='fahemad3@gmail.com',
      license='MIT',
      install_requires=[
          'numpy','pandas','beautifulsoup4','fastnumbers','more-itertools','dill','stockstats','pytidylib','seaborn',
      ],
      keywords=['Pandas','numpy','data-science','IPython', 'Jupyter'],
      packages=find_packages(),
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
