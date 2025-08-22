from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-python-api",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python API with CI/CD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-python-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.3.0",
        "gunicorn>=21.0.0",
    ],
)