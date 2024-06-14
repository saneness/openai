#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import os
import argparse
from openai import OpenAI

def args():
    parser   = argparse.ArgumentParser(description="Wrapper to generate OpenAI messages.")
    parser.add_argument("-m", "--model", metavar="\b", default="gpt-3.5-turbo", help="model to use (default: gpt-3.5-turbo)")
    parser.add_argument("-p", "--prompt", metavar="\b", required=True, help="Prompt to generate response from")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = args()
    client = OpenAI()
    response = client.chat.completions.create(model=args.model, messages=[
        {"role": "user", "content": f"{args.prompt}"}
    ])
    print(f"{response.choices[0].message.content}")
