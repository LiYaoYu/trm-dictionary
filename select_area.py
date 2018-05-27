#!/usr/bin/env python3

# prerequisite: xsel

import subprocess
import time

class Selection:
    def __init__(self, intvl):
        self.content = ""
        self.intvl = intvl

    def get_str(self):
        while True:
            cur = subprocess.check_output(["xsel"])

            if cur == self.content:
                time.sleep(self.intvl)
                continue

            self.content = cur
            return cur.decode()
