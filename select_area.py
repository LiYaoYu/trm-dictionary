#!/usr/bin/env python3

import subprocess
import time

class Selection:
    def __init__(self):
        self.content = ""

    def get(self):
        while True:
            cur = subprocess.check_output(["xsel"])

            if cur == self.content:
                time.sleep(0.25)
                continue

            self.content = cur
            return cur
