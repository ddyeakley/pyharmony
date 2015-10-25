
from setuptools import setup

setup(
    name='harmony',
    version='0.1',
    license='See LICENSE',
    author='Jeff Terrace',
    author_email='Jeff Terrace <jterrace@gmail.com>',
    url='https://github.com/ddyeakley/pyharmony',
    long_description="README.md",
    packages=['auth', 'client'],
    include_package_data=False,
    description="Python library for connecting to and controlling the Logitech Harmony Link",
)