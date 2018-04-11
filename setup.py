try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A simple stopwatch program to help track time on boring, un-automated tasks...',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/super_stopwatch_041118_1',
	'download_url': 'https://github.com/sunnylam13/super_stopwatch_041118_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['time'],
	'scripts': [],
	'name': 'Super Stopwatch'
}

setup(**config)