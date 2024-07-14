---
title: OSCTF 2024 Phantom Script Intrusion forensics challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:19:00+08:00
slug: osctf-2024-phantomscriptintrusion
featured: true
draft: false
tags:
  - forensics
  - ctf
description: Writeup for a obfuscated PHP challenge (forensics) in OSCTF 2024
---


## Solution

We are provided with an obfuscated PHP script, and after deobfuscation we see that ${"GLOBALS"} has a shorturl link. Visiting the link we get the flag.

flag: OSCTF{M4lW4re_0bfU5CAt3d}