"""Pypi software definition"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='argodmqc_owc',
    version='0.1',
    author="argodmqc_owc Developers",
    author_email="?",
    description="A python library to calibrate Argo floats salinity measurements with PWC method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/euroargodev/argodmqc_owc",
    packages=setuptools.find_packages(),
    package_dir={'argodmqc_owc': 'owc_calibration'},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ]
)
