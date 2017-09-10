from setuptools import setup, find_packages

setup(
    name="mediaMix",
    version="0.1",
    author="Ludovic Mandagot, Luka Peschke",
    author_email="ludovic.mandagot@epitech.eu, mail@lukapeschke.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    entry_points= {
        "console_scripts": ["apimedia-server=apiMedia.FluxRSS.Server:start"]
    },
    install_requires=[
        "feedparser",
        "Flask>=0.12",
        "requests",
    ],
)
