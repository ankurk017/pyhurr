import setuptools

with open("README.md", "r") as fn:
    long_description = fn.read()

setuptools.setup(
    name="pyhurr",
    version="0.1.0",
    author="Ankur Kumar, NASA IMPACT and The University of Alabama in Huntsville, UAH, Huntsville, Alabama",
    author_email="ankurk017@gmail.com",
    description="A python package for reading ahps data and plot coastlines .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankurk017/pyhurr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=["cartopy", "matplotlib", "numpy", "xarray"]
)
