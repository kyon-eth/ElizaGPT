from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="elizaGPT",
    version="0.1.0",
    author="Kyon",
    author_email="kyonosuke.eth@gmail.com",
    description="A nostalgic emulation of ELIZA using chatGPT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyon-eth/ElizaGPT",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "rich",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "elizagpt = elizagpt_wrapper.elizagpt:main"
        ]
    },
    scripts=["postinstall.sh"],
)
