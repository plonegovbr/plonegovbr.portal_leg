"""Installer for the plonegovbr.portal_leg package."""
from pathlib import Path
from setuptools import find_namespace_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="plonegovbr.portal_leg",
    version="1.0.0a1",
    description="Uma distribuição Plone para instituições do legislativo brasileiro.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: Distribution",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="PloneGov-Br",
    author_email="portalbrasil@plone.org.br",
    url="https://github.com/plonegovbr/plonegovbr.portal_leg",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/plonegovbr.portal_leg",
        "Source": "https://github.com/plonegovbr/plonegovbr.portal_leg",
        "Tracker": "https://github.com/plonegovbr/plonegovbr.portal/issues",
    },
    license="GPL version 2",
    package_dir={"": "src"},
    packages=find_namespace_packages("src", include=["plonegovbr.*"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Plone",
        "plone.distribution>=1.0.0a9",
        "plone.api",
        "plonegovbr.portal_base",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            "plone.restapi[test]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.2.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_dist_locale = plonegovbr.portal_leg.locales.update:update_locale
    """,
)
