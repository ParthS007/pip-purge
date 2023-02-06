"""
pip-purge manages your requirements files.
"""
from setuptools import setup

setup(
    name="pip-purge",
    version="1.0.0",
    url="https://github.com/kennethreitz/pip-purge",
    license="MIT",
    author="Kenneth Reitz",
    author_email="me@kennethreitz.org",
    MAINTAINER="Parth Shandilya",
    MAINTAINER_EMAIL="parth1989shandilya@gmail.com",
    description=__doc__.strip("\n"),
    scripts=["pip-purge"],
    zip_safe=False,
    platforms="any",
    install_requires=["envoy"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Systems Administration",
    ],
)
