from setuptools import setup

setup(
   name='monke-connection',
   version='1.0',
   description="It's util for http request. It check url and return status code. You can use flag to get more information about url",
   license='MIT',
   author='robotnik-by-rpo',
   author_email='chikindin99@inbox.ru',
   url='https://github.com/robotnik-by-rpo/fossdev/tree/homework/makeutil-pypi',
   packages=['util'], 
   install_requires=[], 
   extras_require={
        'test': [
            'pytest',
            'coverage',
            'requests'
        ],
   },
   python_requires='>=3',
)