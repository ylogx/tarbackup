from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['tarbackup = tarbackup.main:main'],
    },
)

setup(
        name='tarbackup',
        description='Create unique tar backups',
        version='0.0.2',
        packages=['tarbackup'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/tarbackup',
        long_description=open('README.txt').read(),
        **add_keywords
)

