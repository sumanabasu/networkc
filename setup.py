from setuptools import setup

setup(name='networkc',
      version='0.1',
      description='calculates degree, closeness and betweenness centrality and sorts them in descending order',
      url='',
      author='Sumana Basu',
      author_email='sumana.basu@mail.mcgill.ca',
      license='MIT',
      packages=['networkc'],
      install_requires=[
          'networkX', 'pandas', 'matplotlib'
      ],
      zip_safe=False,
      entry_points = {
      'console_scripts':['networkc=networkc.networkc:main']
	  }
      )
