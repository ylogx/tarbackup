from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['tarbackup = tarbackup.main:main'],
    },
)

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()
#print('We require: ', requires)
fhan = open('README.txt')
long_description = fhan.read()
fhan.close()

setup(
        name='tarbackup',
        description='Create unique tar backups',
        version='0.0.3',
        packages=['tarbackup'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/tarbackup',
        long_description=long_description,
        install_requires=requires,
        **add_keywords
)

