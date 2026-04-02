from setuptools import setup

setup(
   name='monkeconn',
   version='1.0',
   description="It's util for http request. It check url and return status code. You can use flag to get more information about url",
   license='MIT',
   author='robotnik-by-rpo',
   author_email='chikindin99@inbox.ru',
   url='https://github.com/robotnik-by-rpo/fossdev/tree/homework/makeutil-pypi',
   packages=['util'], 
   install_requires=['requests'], 
   extras_require={
        'test': [
            'pytest',
            'coverage',
            
        ],
   },
   python_requires='>=3',
)