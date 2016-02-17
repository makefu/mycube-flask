
from setuptools import setup

setup(
    name="mycube-flask",
    version="0.2.3",
    license="Apache2",
    author="makefu",
    author_email="github@syntax-fehler.de",
    packages=["mycube"],
    install_requires = [
        "Flask",
        "redis",
    ],
    entry_points={
        'console_scripts' : [
            'mycube-simple = mycube.wsgi:main'
        ]
    },
    url="http://github.com/makefu/mycube-flask",
)
