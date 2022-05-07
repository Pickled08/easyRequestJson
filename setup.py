from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Easy Post and Get requests'
LONG_DESCRIPTION = 'An easy way to do Get and Post requests'

setup(
        name="easyRequestJson", 
        version=VERSION,
        author="Pickled08",
        author_email="alexhoward21@icloud.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests"]
)