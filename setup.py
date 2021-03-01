import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pvaw",
    version="0.0.1",
    author="Michael Petro",
    author_email="mgpetro99@gmail.com",
    description="Python Wrapper for the NHTSA Vehicle API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelmicheal/PythonVehicleAPIWrapper",
    install_requires=["pandas", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["pvaw"],
    python_requires=">=3.6",
)
