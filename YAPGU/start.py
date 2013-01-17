"""
Advanced Start Main File - ASME (oh oh oh, ASM!).
Calls start function from module main (so suprising).
"""

import sys
import main
if __name__ == "__main__":
    main.start(sys.argv)
else:
    raise RuntimeError("No one simply imports start module.")

