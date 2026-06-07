"""
n8n Workflow Automation Project Setup

This module provides setup utilities for the n8n workflow automation project.
"""

from setuptools import setup, find_packages

setup(
    name="n8n-workflow-automation",
    version="1.0.0",
    description="Comprehensive guide to n8n workflow automation with hands-on examples",
    author="Cavin Otieno",
    author_email="cavin.otieno012@gmail.com",
    url="https://github.com/OumaCavin/n8n-workflow-automation",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pytest>=7.0.0",
    ],
    extras_require={
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pytest-cov>=4.0.0",
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=8.5.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="n8n workflow automation api integration",
    project_urls={
        "Bug Reports": "https://github.com/OumaCavin/n8n-workflow-automation/issues",
        "Source": "https://github.com/OumaCavin/n8n-workflow-automation",
    },
)