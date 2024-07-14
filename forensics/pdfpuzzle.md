---
title: OSCTF 2024 PDF Puzzle forensics challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:21:00+08:00
slug: osctf-2024-pdfpuzzle
featured: true
draft: false
tags:
  - forensics
  - ctf
description: Writeup for a metadata challenge (forensics) in OSCTF 2024
---


## Solution

Using exiftool or otherwise, check the metadata of the file. The flag is stored under Author.

flag: OSCTF{H3il_M3taD4tA}