mchain
======

mchain is a web application which provides Human readable text generator based on Markov chains based on any corpus text. Application uses a JSON-RPC protocol.

Parameters are:
* crp - string with corpus text
* dgr - degree. Length of generator key
* mwr - maximal length of generated text (in words)

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
    