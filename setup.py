try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A simple stopwatch program to help track time on boring, un-automated tasks...',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Super Stopwatch'
}

setup(**config)