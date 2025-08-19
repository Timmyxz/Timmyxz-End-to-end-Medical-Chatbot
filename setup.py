from setuptools import setup, find_packages

setup(
    name="medical-chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Dependencies are managed in requirements.txt
    ],
    python_requires=">=3.10,<3.13",
    author="Timmyxz",
    description="An end-to-end medical chatbot implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)