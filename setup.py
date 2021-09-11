import setuptools

AUTHOR = "JAK (Jonak Adipta Kalita)"
VERSION = "1.0.2"
DESCRIPTION = "A Python Package made by JAK!!"
AUTHOR_EMAIL = "<jonakadiptakalita@gmail.com>"
URL = "https://github.com/Jonak-Adipta-Kalita/JAK-Python-Package"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="beast-night-tv",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    install_requires=[],
    url=URL,
    keywords=["python", "first_package", "edit_message"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
