#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import argparse
import json
import os
from openai import OpenAI

def args():
    parser   = argparse.ArgumentParser(description="Wrapper to generate OpenAI messages.")
    parser.add_argument("-u", "--user", metavar="\b", required=True, help="user to get conversation history for")
    parser.add_argument("-l", "--log",  metavar="\b", default="/tmp", help="conversation logs")
    parser.add_argument("-m", "--model", metavar="\b", default="gpt-3.5-turbo", help="model to use (default: gpt-3.5-turbo)")
    parser.add_argument("-p", "--prompt", metavar="\b", required=True, help="Prompt to generate response from")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = args()
    messages = []
    history = f"{args.log}/{args.user}"
    if os.path.isfile(history):
        messages = json.loads(open(history).read().strip())
    messages.append(
        {"role": "user", "content": f"{args.prompt}"}
    )
    client = OpenAI()
    response = client.chat.completions.create(model=args.model, messages=messages).choices[0].message.content
    messages.append(
        {"role": "assistant", "content": f"{response}"}
    )
    open(history, "w+").write(json.dumps(messages))
    print(f"{response}")
