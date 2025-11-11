from setuptools import setup, find_packages

setup(
    name="prompt-optimizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai>=0.5.0",
    ],
    entry_points={
        "console_scripts": [
            "prompt-optimizer=prompt_optimizer.PromptOptimizer:main",
        ],
    },
    author="Dushmilan",
    author_email="Dushmilan05@gmail.com",
    description="A CLI tool to optimize prompts using Google Generative AI",
    long_description=open("README.Md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dushmilan/prompt-optimizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)