import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME="Suvarn14"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL="suvarnsrivatsa14@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small Python Pacakage for CNN application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Suvarn14/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/Suvarn14/Text-Summarizer/issues",
    },
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where="src"),
)
