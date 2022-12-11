# ElizaGPT - AI rogerian psychotherapist


ElizaGPT is a simulation of Eliza, an early natural language processing computer program created from 1964 to 1966 at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum. Under the hood it uses an unofficial API that lets you interact with the OpenAI ChatGPT in Python and as a CLI.

https://user-images.githubusercontent.com/99987044/206916707-c6e9f7b5-28f2-44cd-81f1-7ff96183e793.MP4


## How it works

Here's an example of how to use the ElizaGPT Wrapper on the command line:

Run an interactive session in the terminal by using

``` bash
$ elizagpt
```

Or get the response for one question

``` bash
$ elizagpt Why am I feeling blue?
```


## Requirements

To use this repository, you will need to have the following packages installed:

`setuptools`: This package is used to create and manage Python packages.
You can install it using `pip install setuptools`.

## Installation

Clone this repository and install the required dependencies:

```bash
pip install git+https://github.com/kyon-eth/ElizaGPT
```

Setup the script by logging in to your openai account for the first time only.

```bash
elizagpt install
```

## Usage

### Shell

The `elizagpt` command can be run in the shell, allowing you to have a conversation with ElizaGPT directly in the terminal. Simply run the command and start chatting!

The shell includes some nice features:
* It provides commands to navigate to past points in the conversation.
* It provides a command to start new conversations.
* It allows the user to choose between markdown and streaming output.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project is a modification from [Mabrouk](https://github.com/mmabrouk/chatgpt-wrapper) code which is modification of [Taranjeet](https://github.com/taranjeet/chatgpt-api) code which is a modification of [Daniel Gross](https://github.com/danielgross/whatsapp-gpt) code.

