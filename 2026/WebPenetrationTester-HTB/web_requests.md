## WEB REQUESTS 

### Tuesday, 23 June 2026
Let's start with choose a JOB ROLE PATH in HackTheBox?? **"Web Penetration Tester."**

- The first question in section 1/8.<br>
  "Use curl and download the file returned in the specified path"
     1. I try it using web browser, and it's just returned a text and suggest me to using cURL
     2. then I try using:
         ```bash
         curl TARGET_IP/download.php
         ```
- The second question in section 3/8 can also be done by sending any error requests, then server will response with what version of Apache server is running.
- cURL:
     - `-v`    ⇒ verbose
     - `-I`    ⇒ to send a HEAD request and only display the response headers.
     - `-i`    ⇒ to send a HEAD request and display both the headers and response body
     - `-s`    ⇒ did not print the download/upload status, I guess
---
### Wednesday, 24 June 2026
- **HTTP Headers**

     | Category             |  Request | Response | Used to              | Example |
     |----------------------|:--------:|:--------:|----------------------|---------|
     | **General Headers**  |     ✔    |     ✔    | describe message     | `Date: Wed, 24 June 2026 10:38:44 GMT` |
     |                      |          |          |                      |`Connection: close` |
     | **Entity Headers**   |     ✔    |     ✔    | describe the content | `Content-Type: text/html` |
     |                      |          |          |                      |`Media-Type: application/pdf` |
     |                      |          |          |                      |`boundary="b4e4fbd93540"` |
     | **Request Headers**  |     ✔    |          | provide critical metadata about the request | `Host: www.inlanefreight.com` |
     |                      |          |          |                      |`Cookie: PHPSESSID=b4e4fbd93540` |
     |                      |          |          |                      |`Authorization: BASIC cGFzc3dvcmQK` |
     | **Response Headers** |          |     ✔    | provide context about the returned data | `Server: Apache/2.2.14 (Win32)` |
     |                      |          |          |                      |`Set-Cookie: PHPSESSID=b4e4fbd93540` |
     |                      |          |          |                      |`WWW-Authenticate: BASIC realm="localhost"` |
     | **Security Headers** |          |     ✔    | specify certain rules and policies | `Content-Security-Policy: script-src 'self'` |
     |                      |          |          |                      |`Strict-Transport-Security: max-age=31536000` |
     |                      |          |          |                      |`Referrer-Policy: origin` |

- **cURL :**  
     - `-k`    ⇒ skip the certificate checks

     - `-v`    ⇒ shows us the full details of the HTTP request and response. 
     - `-I`    ⇒ to send a HEAD request and only display the response headers.
     - `-i`    ⇒ to send a HEAD request and display both the headers and response body
     - `-H`    ⇒ to set our request headers
     - `-A`    ⇒ to set our User-Agent
     - `-s`    ⇒ did not print the download/upload status, I guess
---
### Friday, 26 June 2026
- The question in section 4/8,
     1. Open the Network tab in web dev-tool after the page loaded.
     2. See the `/flag_xxx` file, then paste it into the url
- Most commonly used request methods:
     - `GET`
     - `POST`
     - `HEAD`
     - `PUT`        ⇒ create new resources on the server
     - `DELETE`	
     - `OPTIONS`    ⇒ returns information about the server
     - `PATCH`      ⇒ applies partial modifications to the resource
---
### Saturday, 27 June 2026
- Status Codes
     - `1xx`   provides INFO, and do not affect the proccess of the request
     - `2xx`   returned when the request SUCCEEDS
     - `3xx`   returned when the server REDIRECT the client
     - `4xx`   signifies IMPROPER REQUESTS from client
     - `5xx`   returned when there is a PROBLEM FROM the HTTP SERVER itself<br>

  &#x21AA; commonly seen:
     - `200 OK`
     - `302 Found`       : redirect the client to another URL, like redirecting the user to dashboard after a successful login
     - `400 Bad Request` : malformed requests such as requests with missing line terminators
     - `403 Forbidden`   : signifies that the client doesn't have appropriate access
     - `404 Not Found`
     - `500 Internal Server Error`

  >**note:** Apart from the standard HTTP codes, various servers and providers such as Cloudflare or AWS implement their own codes

- HTTP basic Auth
     ```
     $ curl -i TARGET_IP    # -i to display the response header        
	HTTP/1.1 401 Authorization Required
	Date: Sat, 27 Jun 2026 16:35:03 GMT
	Server: Apache/2.4.41 (Ubuntu)
	Cache-Control: no-cache, must-revalidate, max-age=0
	WWW-Authenticate: Basic realm="Access denied"
	Content-Length: 13
	Content-Type: text/html; charset=UTF-8

	Access denied
     ...
     # To provide the credentials through cURL, we can use the -u flag

     $ curl -u admin:admin TARGET_IP -v    # then I add -v to show the response header aswell
	*   ...
	* Established connection to TARGET_IP (...) from 10.0.2.15 port 57624 
	* using HTTP/1.x
	* Server auth using Basic with user 'admin'
	> GET / HTTP/1.1
	> Host: ...
	> Authorization: Basic YWRtaW46YWRtaW4=
	> User-Agent: curl/8.20.0
	> Accept: */*
	> ... 
     ```
     Honestly idk what to do here, so I try open it using browser and try search something and then in the Network tab of dev-tool,
     it shown the path to search.php<br>
     and finally..
     ```
     curl http://TARGET_IP/search.php?search=flag -u admin:admin    # it should show the flag 
	```
---
### Monday, 29 June 2026
- Question 1 in section 7/8.<br>
  \`Obtain a session cookie through a valid login, and then use the cookie with cURL to search for the flag through a JSON POST request to `/search.php`. Authenticate to 154.57.164.63 , with user "admin" and password "admin."\` 
     ```
     $ curl  http://TARGET_IP/ -v
        ...
        <form method="post">
            <input type="text" name="username" placeholder="Username" required="required" />
            <input type="password" name="password" placeholder="Password" required="required" />
            <button type="submit" class="btn btn-primary btn-block btn-large">Login</button>
        </form>
        ...
     # need a POST requests method with username and password data to be sent
     $ curl  -X POST -d 'username=admin&password=admin' http://TARGET_IP/ -v
	...
	< Set-Cookie: PHPSESSID=dthnimjmb4l73ud6gg5uc3i0c4; path=/ 
	...
     $ curl -X POST -b 'PHPSESSID=dthnimjmb4l73ud6gg5uc3i0c4' http://TARGET_IP/search.php?search=flag
	Content type must be: application/json

     $ curl -X POST -b 'PHPSESSID=dthnimjmb4l73ud6gg5uc3i0c4' -H 'Content-Type: application/json' http://TARGET_IP/search.php 
	POST data is empty

     $ curl -X POST -d '{"search":"flag"}' -b 'PHPSESSID=dthnimjmb4l73ud6gg5uc3i0c4' -H 'Content-Type: application/json' http://TARGET_IP/search.php
	["flag: HTB{xxxx}"]

- another **CURL** flags:  
     - `-X`    ⇒ request method like GET, POST, PUT
	- `-H`    ⇒ headers
     - `-d`    ⇒ if we need a data to send
     - `-b`    ⇒ cookies
          >still confuse about this part..<BR> either I need `{}` or not, and `:` or `=`

---
### Tuesday, 30 June 2026
- CRUD APIs
     | Operation | HTTP Method | Description |
     |-----------|-------------|-------------|
     | Create    | POST	       | Adds the specified data to the database table |
     | Read      | GET         | Reads the specified entity from the database table |
     | Update    | PUT         | Updates the data of the specified database table |
     | Delete    | DELETE      | Removes the specified row from the database table |
     
- Question 1 in section 8/8.<br>
  "First, try to update any city's name to be 'flag'. Then, delete any city. Once done, search for a city named 'flag' to get the flag."<br>
  
  &#x21AA; There's how I complete the Question:
     ```
     $ curl http://TARGET_IP/api.php/city/    
	[{"city_name":"London","country_name":"(UK)"},{"city_name":"Birmingham","country_name":"(UK)"}, ...

     $ curl -X POST http://TARGET_IP/api.php/city/London -d '{"city_name":"flag","country_name":"flag"}' -H 'Content-Type: application/json'

     $ curl http://TARGET_IP/api.php/city/flag   
	[{"city_name":"flag","country_name":"flag"}]

     $ curl -X DELETE http://TARGET_IP/api.php/city/London 

     $ curl http://TARGET_IP/api.php/city/flag            
	[{"city_name":"flag","country_name":"HTB{XXXXXXX}"}]
     ```

---
 https://academy.hackthebox.com/achievement/1729031/35
