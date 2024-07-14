---
title: OSCTF 2024 Style Query Listing web challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:27:00+08:00
slug: osctf-2024-stylequerylisting
featured: true
draft: false
tags:
  - web
  - ctf
description: Writeup for a SQL challenge (web) in OSCTF 2024
---


## Solution

Style Query Listing -> SQL
Try something simple like 
admin' or 1==1 --

Site throws exception, which can be used to see source code.
```python
if username == 'admin':
    return redirect(url_for('admin'))
```

Go to /admin for the flag.

flag: OSCTF{D1r3ct0RY_BrU7t1nG_4nD_SQL}