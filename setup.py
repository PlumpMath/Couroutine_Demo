try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Generator Test',
    'author': 'Noel Niles',
    'url': 'noelniles.com/downloads/software/NAME',
    'download_url': 'Where to download it.',
    'author_email': 'noelniles@gmail.com',
    'version': '0.0.0.1',
    'install_requires': ['nose'],
    'packages': ['gent'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
