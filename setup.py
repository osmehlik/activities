from setuptools import setup, find_packages

setup(
    name="activities",
    version='0.0.1',
    author="Oldřich Šmehlík",
    author_email="oldrich@smehlik.net",
    packages=find_packages(include=['activities', 'activities.*']),
    entry_points={
        'console_scripts': ['activities-cli=activities.app:main']
    }
)
