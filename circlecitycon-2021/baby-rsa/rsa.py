#!/usr/bin/env python3
import gmpy
from Cryptodome.Util import number

plain, _ =gmpy.root(80505397907128518326368510654343095894448384569115420624567650731853204381479599216226376345254941090872832963619259274943986478887206647256170253591735005504, 3)
print(number.long_to_bytes(int(plain)))