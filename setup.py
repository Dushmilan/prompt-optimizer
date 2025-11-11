from setuptools import setup, find_packages
import os

# Read README.md
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "A CLI tool to optimize prompts using Google Generative AI"

# Read requirements.txt
requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
if os.path.exists(requirements_path):
    with open(requirements_path, "r", encoding="utf-8") as fh:
        requirements = fh.read().splitlines()
else:
    requirements = ["google-generativeai>=0.5.0"]

setup(
    name="prompt-optimizer",
    version="0.1.0",
    author="Dushmilan",
    author_email="Dushmilan05@gmail.com",
    description="A CLI tool to optimize prompts using Google Generative AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dushmilan/prompt-optimizer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "prompt-optimizer=prompt_optimizer.optimizer:main",
        ],
    },
)