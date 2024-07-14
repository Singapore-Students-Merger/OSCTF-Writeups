---
title: OSCTF 2024 Indoor WebApp web challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:27:00+08:00
slug: osctf-2024-indoorwebapp
featured: true
draft: false
tags:
  - web
  - ctf
description: Writeup for a web sanity check (web) in OSCTF 2024
---


## Solution

Button on homepage takes us to `/profile?user_id=1`
Trying `/profile?user_id=2` gives us the flag.

flag: OSCTF{1nd00r_M4dE_n0_5enS3}