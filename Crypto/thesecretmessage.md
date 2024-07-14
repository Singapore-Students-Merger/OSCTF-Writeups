---
title: OSCTF 2024 The Secret Message cryptography challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T17:29:00+08:00
slug: osctf-2024-thesecretmessage
featured: true
draft: false
tags:
  - crypto
  - ctf
description: Writeup for a RSA challenge (crypto) in OSCTF 2024
---


## Solution

We notice that e = 3. Hence we just need to cube root it.

```python
from sympy import integer_nthroot
n = 9552920989545630222570490647934784790995742371314697500156637473945512219140487351
e = 3
c = 1234558821525449682631051062047285610559270618375596181404770970780385739
p, a = integer_nthroot(c, e)
if a:
    print(p)
else:
    print("ERROR")

print(p.to_bytes((p.bit_length() + 7) // 8, 'big'))
```

flag: OSCTF{Cub3_R00Ting_RSA!!}