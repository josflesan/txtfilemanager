from setuptools import setup


setup(
    name="txtfilemanager",
    version="0.0.1",
    author="Lemurer",
    author_email="lemurercompany@gmail.com",
    description="Allow the easy manipulation of text files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alestiago/txtfilemanager",
    py_modules=["txtfilemanager"],
    package_dir={"":"src"},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
