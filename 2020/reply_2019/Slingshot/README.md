# Slingshot

The page seems inaccessible from an exernal user, so we need to spoof the IP of the source in order to get right response. We can use `X-Forwarded-For` header field inside the request in order to change the source. We can change it to `192.168.1.2`, and as a result we will get the login page.

Now, if we run a nikto scan (remember to change the header of the request also in nikto with 
```
nl=$'\n'
cr=$'\r'
nikto -host http://example.com/ -useragent "nikto${cr}${nl}X-Forwarded-For: 192.168.1.2"

```
), we find an interesting backup file `backup.tar`.