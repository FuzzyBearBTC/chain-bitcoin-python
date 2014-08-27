from distutils.core import setup
import os.path

dirname = os.path.dirname(__file__)


def resolve_path(path):
    return os.path.join(dirname, path)


def read_lines(path):
    with open(resolve_path(path)) as f:
        return f.readlines()

setup(
    name='chain_bitcoin',
    version='0.1',
    packages=['chain_bitcoin'],
    url='https://github.com/cardforcoin/chain-bitcoin-python',
    license='MIT',
    description='Integration library for the Chain.com API',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=read_lines('requirements-install.txt'),
    tests_require=read_lines('requirements-test.txt'),
)
