mchain
======

**mchain** is a Python module providing human readable text generator using Markov chains based on any corpus text.

### Installation

    cd ./mchain
    python setup.py build
    sudo python setup.py install

### Basic usage

    >>> from mchain.mchain import Mchain
    >>> mc = Mchain()
    >>> mc.generate('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tristique ipsum nec mauris iaculis, vitae.', 1, 10)
    'Lorem ipsum nec mauris iaculis, vitae.'

For best results use generator key equal or longer than 3 and corpus text longer that 5000 characters.

### Web application

This repository provides also an example of web application using mchain. Application uses JSON-RPC protocol.

Parameters are:

* crp - string with corpus text
* dgr - degree. Length of generator key
* mwr - maximal length of generated text (in words)

Call specification:

    {
        "jsonrpc": "2.0",
        "method": "generate",
        "id": "json-rpc-call-d",
        "params": [crp, dgr, mwr]
    }

Sample call:

    {
        "jsonrpc": "2.0",
        "method": "generate",
        "id": "12345-abcde",
        "params": [
            "Lorem ipsum dolor sit amet",
            2,
            10
        ]
    }