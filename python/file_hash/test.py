#!/usr/bin/env python3


import sys
import hashlib


def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


f1_hash = hashfile(sys.argv[1])
f2_hash = hashfile(sys.argv[2])

print("{0} hash: {1}".format(sys.argv[1], f1_hash))
print("{0} hash: {1}".format(sys.argv[2], f2_hash))

if f1_hash == f2_hash:
    print("Both hashes are same")
else:
    print("File hashes are different")
