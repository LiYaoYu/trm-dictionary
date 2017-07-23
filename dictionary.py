#!/usr/bin/env python3

import select_area


def main():
    m = select_area.Selection()
    while True:
        print(m.get())


if __name__ == "__main__":
    main()
