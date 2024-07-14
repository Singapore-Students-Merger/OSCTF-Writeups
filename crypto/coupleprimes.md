---
title: OSCTF 2024 Couple Primes cryptography challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T17:33:00+08:00
slug: osctf-2024-coupleprimes
featured: true
draft: false
tags:
  - crypto
  - ctf
description: Writeup for a RSA challenge (crypto) in OSCTF 2024
---


## Solution

Very basic RSA, solve script below

```python
from Crypto.Util.number import *
from sympy import isprime, nextprime, mod_inverse
from sympy.ntheory import factorint

n = 2015988416886389917712817571503042966646173328566017066425504857911626508776326874
c = 1844016236801024937565334867742959522905118003566884500112585504875059105978563086
e = 65537

f = factorint(n)
p, q = f.keys()
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

m = pow(c, d, n)
m = long_to_bytes(m)
print(m.decode)
```

flag: OSCTF{m4y_7h3_pR1m3_10v3_34cH_07h3r?}