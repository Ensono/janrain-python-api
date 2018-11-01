import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="janrain-python-api",
    version="0.0.1",
    author="Lewis England",
    author_email="lewis.england@amido.com",
    description="A simple wrapper around Janrain's config API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amido/janrain-python-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)