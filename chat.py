#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import math
import os
from openai import OpenAI

def args():
    parser   = argparse.ArgumentParser(description="Wrapper to generate OpenAI messages.")
    parser.add_argument("-u", "--user", metavar="\b", help="user to get conversation history for")
    parser.add_argument("-l", "--log",  metavar="\b", default="/tmp", help="conversation logs")
    parser.add_argument("-m", "--model", metavar="\b", default="gpt-4o", help="model to use (default: gpt-4o)")
    parser.add_argument("-p", "--prompt", metavar="\b", help="Prompt to generate response from")
    parser.add_argument("-c", "--clean", action="store_true", help="Run clean checks for all the chats")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = args()
    if not args.clean:
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
    else:
        history = f"{args.log}"
        for user in os.listdir(history):
            log = os.path.join(history, user)
            if os.path.isfile(log):
                size = os.path.getsize(log) / 1024
                # exponential formula for storage time
                # X1 = 40
                # Y1 =  1
                # X2 =  4
                # Y2 = 10
                # W  = -0.1
                # time = (Y2-Y1)*(math.exp(W*size)-math.exp(W*X1))/(math.exp(W*X2)-math.exp(W*X1)) + Y1 
                time = 1
                mtime = (datetime.datetime.now().timestamp() - os.path.getmtime(log)) / 3600
                if mtime > time:
                    os.remove(log)
