
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
        "flup",
        "redis",
    ],
    url="http://github.com/makefu/mycube-flask",
    package_data = {"mycube": ["*.fcgi"] },
)