#!/usr/bin/env python3

import select_area, query

INTERVAL = 0.2

def main():
    hl = select_area.Selection(INTERVAL)
    qr = query.Query()

    while True:
        word = hl.get_str()
        xlate = qr.qr_gxlate(word)
        print(xlate)
        print(qr.get_gelapsed())

if __name__ == "__main__":
    main()
