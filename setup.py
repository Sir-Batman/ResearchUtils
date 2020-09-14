import setuptools

with open("README.md", 'r') as fh:
    long_desc = fh.read()

setuptools.setup(
    name="research-utils-yatesco",
    version="0.0.1",
    author="Connor Yates",
    author_email="yatesco@oregonstate.edu",
    description="A collection of useful utilities that make simulation research easier and safer",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)
