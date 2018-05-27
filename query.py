#!/usr/bin/env python3

# prerequisite: googletrans

import googletrans
import time

class Query:
    def __init__(self):
        self.gbeg_t = 0
        self.gend_t = 0

        self.ybeg_t = 0
        self.yend_t = 0

    def qr_gxlate(self, s):
        self.gbeg_t = time.time()
        translator = googletrans.Translator()
        res = translator.translate(s).text
        self.gend_t = time.time()
            
        return res

    def get_gelapsed(self):
        return self.gend_t - self.gbeg_t
        



def main():
    qr = Query()
    while True:
        xlate = qr.qr_gxlate("翻譯")
        print(xlate)
        print(qr.get_gelapsed())

if __name__ == "__main__":
    main()
