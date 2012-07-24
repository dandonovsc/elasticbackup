from setuptools import setup, find_packages

setup(
    name = 'esbackup',
    version = '0.0.1',
    packages = find_packages(),

    # metadata for upload to PyPI
    author = 'Nick Stenning',
    author_email = 'nick@whiteink.com',
    url = 'https://github.com/nickstenning/esbackup',
    description = 'esbackup: tools to backup and restore ElasticSearch indices',
    license = 'MIT',
    keywords = 'sysadmin elasticsearch backup restore',

    install_requires = [
        'requests==0.13.3',
    ],

    entry_points = {
        'console_scripts': [
            'esbackup = esbackup:main',
            'esrestore = esrestore:main'
        ]
    }
)
