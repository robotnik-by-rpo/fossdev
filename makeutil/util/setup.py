from setuptools import setup, find_packages

setup(
    name = "http_conn",
    version = "0.0.0",
    package_dir = {"": "src"},
    packages = find_packages(where="src")
)