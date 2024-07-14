---
title: OSCTF 2024 Seele Vellorei forensics challenge writeup
author: yanganyi
pubDatetime: 2024-07-14T13:22:00+08:00
slug: osctf-2024-seelevellorei
featured: true
draft: false
tags:
  - forensics
  - ctf
description: Writeup for a binwalk challenge (forensics) in OSCTF 2024
---


## Solution

Use binwalk to extract all files inside the .docx, proceed to document.xml and grep for the flag.

flag:  OSCTF{V3l10n4_1s_Gr43t}