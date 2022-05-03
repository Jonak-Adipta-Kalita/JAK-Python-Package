import setuptools

AUTHOR = "JAK (Jonak Adipta Kalita)"
VERSION = "2.0.0"
DESCRIPTION = "A Python Package made by JAK!!"
AUTHOR_EMAIL = "<jonakadiptakalita@gmail.com>"
URL = "https://github.com/Jonak-Adipta-Kalita/JAK-Python-Package"
INSTALL_REQUIRES = []
PROJECT_URLS = {
    "Documentation": "https://jak-python-package.readthedocs.io/",
    "Issue tracker": "https://github.com/Jonak-Adipta-Kalita/JAK-Python-Package/issues",
}
KEYWORDS = ["python", "first_package", "edit_message"]
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

if __name__ == "__main__":
    setuptools.setup(
        name="beast-night-tv",
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=setuptools.find_packages(),
        install_requires=INSTALL_REQUIRES,
        url=URL,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
    )
