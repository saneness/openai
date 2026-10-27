#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

import base64, secrets
import os
import argparse
from openai import OpenAI
from config import *

def args():
    parser   = argparse.ArgumentParser(description="Wrapper to generate OpenAI images.")
    parser.add_argument("-m", "--model", metavar="\b", default="gpt-image-2.5-sunburst", help="model to use (default: gpt-image-2.5-sunburst)")
    parser.add_argument("-s", "--size", metavar="\b", default="1024x1024", help="size to use (default: 1024x1024)")
    parser.add_argument("-p", "--prompt", metavar="\b", required=True, help="Prompt to generate image from")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = args()
    client = OpenAI()
    response = client.images.generate(model=args.model, prompt=args.prompt, size=args.size, quality="auto", n=1)
    name = f"{secrets.token_urlsafe(16)}.png"
    open(f"{OUT_DIR}/{name}", "wb").write(base64.b64decode(response.data[0].b64_json))
    print(f"{BASE_URL}/{name}")

    
    
