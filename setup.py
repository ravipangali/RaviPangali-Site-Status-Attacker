# setup.py
from setuptools import setup, find_packages

setup(
    name="ravipangali-sites-status-attacker",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="A django package made by Ravi Pangali for down those sites which are made by himself",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ravi Pangali",
    author_email="legendromeoravi@gmail.com",
    url="https://github.com/ravipangali/RaviPangali-Site-Status-Attacker",
    install_requires=[
        "Django>=5.2.1",
        "djangorestframework>=3.16.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
    ],
    package_data={
        "ravipangali_sites_status_attacker": [
            "templates/*.html",
        ],
    },
)