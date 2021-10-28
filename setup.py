from setuptools import setup, find_packages

setup(
    name='activities',
    description='A simple command line time tracker',
    version='0.0.1',
    license='BSD 2-Clause License',
    author='Oldřich Šmehlík',
    author_email='oldrich@smehlik.net',
    url='https://github.com/osmehlik/activities',
    packages=find_packages(include=['activities', 'activities.*']),
    entry_points={
        'console_scripts': ['activities-cli=activities.app:main']
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3'
    ]
)
