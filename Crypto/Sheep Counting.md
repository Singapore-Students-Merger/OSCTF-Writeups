```python
png_magic = bytes.fromhex('89504E470D0A1A0A0000000D49484452')
# magic 89 50 4E 47 0D 0A 1A 0A
# ihdr 00 00 00 0D 49 48 44 52
```

https://en.wikipedia.org/wiki/PNG

 .png file so first 16 bytes should follow magic bytes + IHDR if its standard
 xor with that and we get keystream, since ECB should be same key xor all the way

https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'0b01c106a697431ecfe8adbc270c70a7'%7D,'Standard',false)&oeol=CR

![Screenshot_from_2024-07-13_19-11-14](https://github.com/user-attachments/assets/b2fa03c3-2c5a-4e23-b32d-51a2001a2796)
