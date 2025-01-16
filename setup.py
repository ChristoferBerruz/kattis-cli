from setuptools import setup

setup(
    name='kattis-cli',
    version='0.1.0',
    author='Christofer Washington Berruz Chungata',
    author_email='cberruzc@my.bridgeport.edu',
    description='A CLI tool for Kattis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChristoferBerruz/kattis-cli',
    py_modules=['submit'],
    entry_points={
        'console_scripts': [
            'kattis-cli=submit:main',
        ],
    },
    install_requires=[
        'requests',
        "lxml",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
