---
title: OSCTF 2024 Mysterious Website Incident forensics challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:17:00+08:00
slug: osctf-2024-mysteriouswebsiteincident
featured: true
draft: false
tags:
  - forensics
  - ctf
description: Writeup for a nginx log challenge (forensics) in OSCTF 2024
---


## Solution

We are presented with a nginx log. Look for suspicious links, there is a Google Drive Link which leads us to the flag.

flag: OSCTF{1_c4N_L0g!}