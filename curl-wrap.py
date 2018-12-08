#!/usr/bin/env python3

from subprocess import call

if __name__ == "__main__":
    call(["curl","https://tools.ietf.org/rfc/rfc1149.txt", "-o", "foo.txt"])