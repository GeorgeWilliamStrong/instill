from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='instill-sdk-prototype',
    version='0.1.0',
    description='Instill AI Python SDK Prototype',
    long_description='This package provides a prototype SDK for interacting with Instill AI services, including Artifact, Model, and Pipeline. It supports dual initialization methods: direct service initialization and centralized configuration through Core.',
    author='George Strong',
    author_email='george.strong@instill.tech',
    python_requires='==3.11.*',
    packages=find_packages(),
    install_requires=required)
