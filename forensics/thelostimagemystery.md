---
title: OSCTF 2024 The Lost Image Mystery forensics challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:12:00+08:00
slug: osctf-2024-thelostimagemystery
featured: true
draft: false
tags:
  - forensics
  - ctf
description: Writeup for a corrupted image header challenge (forensics) in OSCTF 2024
---


## Solution

A corrupted image is provided, we can use hexed.it to check the hex values. Noticing "IF" would hint that its a JPEG file as the JPEG file header includes "JFIF". We can then easily edit the hex value and open the image to get the flag.

flag: OSCTF{W0ah_F1l3_h34D3r5}