from setuptools import setup

setup(
    name='b3Crypt',
    version='0.1.0',
    description='A Python encryption module',
    author='Thomas While',
    author_email='tominko.nelko@gmail.com',
    packages=['b3Crypt'],
    install_requires=[
        'cryptography'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
