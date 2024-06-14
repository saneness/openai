#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import os
import argparse
from openai import OpenAI

def args():
    parser   = argparse.ArgumentParser(description="Wrapper to generate OpenAI images.")
    parser.add_argument("-m", "--model", metavar="\b", default="dall-e-3", help="model to use (default: dall-e-3)")
    parser.add_argument("-s", "--size", metavar="\b", default="1024x1024", help="size to use (default: 1024x1024)")
    parser.add_argument("-p", "--prompt", metavar="\b", required=True, help="Prompt to generate image from")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = args()
    client = OpenAI()
    response = client.images.generate(model=args.model, prompt=args.prompt, size=args.size, quality="standard", style="natural", n=1)
    print(f"```revised_prompt\n{response.data[0].revised_prompt}\n```")
    print(f"{response.data[0].url}")
