from setuptools import setup, find_packages

setup(
    name="tax",
    version="0.0.0",
    package_dir={"": "src"},
    install_requires=[],
    packages=find_packages(where="src")
)