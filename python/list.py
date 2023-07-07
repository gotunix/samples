#!/usr/bin/env python3

import pathlib

theshits = pathlib.Path("python")

for item in theshits.rglob("*"):
    print(f"{item} - {'dir' if item.is_dir() else 'file'}")
