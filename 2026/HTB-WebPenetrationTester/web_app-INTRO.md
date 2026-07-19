
## INTRODUCTION TO WEB APPLICATIONS

###  Saturday, 11 July 2026
#### Web Applications vs Websites vs Native OS Applications

Web App:
  - Dynamic pages
  - Interactive
  - Different view for each users
  - Can run in a browser / no installation needed
  - Can be updated in a single location (webserver) 
 
Websites:
  - Can run in a browser / no installation needed
  - Can be updated in a single location (webserver) 
  - Static pages
  - Same for everyone

Native OS Applications
  - Faster to load and interact with
  - Can utilize native operating system libraries and local hardware
  - Manually update by each users
  - Need to be installed in user's system

...

---
#### Web Application Distribution

There are many open-source web applications used by organizations worldwide that can be customized to meet each organization's needs.<br>
Some common open source web applications include:
  - `WordPress`
  - `OpenCart`
  - `Joomla`

#### Web Application Infrastructure
    
Web applications can use many different infrastructure setups. These are also called `models`. <br>
The most common ones can be grouped into the following four types:
  - Client-Server<br>
    Web applications often adopt the client-server model. A server hosts the web application in a client-server model and distributes it to any clients trying to access it.
  - One Server<br>
    The entire web application or even several web applications and their components, including the database, are hosted on a single server. Though this design is straightforward and easy to implement, it is also the riskiest design.
  - Many Servers - One Database
  - Many Servers - Many Databases

  Aside from these models, there are other web application models available such as serverless web applications or web applications that utilize microservices.

#### Web Application Components

  - `Client`
  - `Server`
    - Webserver
    - Web Application Logic
    - Database
  - `Services` (Microservices)
    - 3rd Party Integrations
    - Web Application Integrations
  - `Functions` (Serverless)

#### Web Application Architecture

  - Presentation Layer
  - Application Layer
  - Data Layer

Furthermore, some web servers can run operating system calls and programs, like IIS ISAPI or PHP-CGI.

...


---
#### Front End

Usually include `HTML`, `CSS`, and `JavaScript`.

Aside from that. These are some of the other tasks related to front end web application development:
  - Visual Concept Web Design
  - User Interface (UI) design
  - User Experience (UX) design

---
###  Monday, 13 July 2026

These mistakes lead to the **`OWASP Top 10`** vulnerabilities for web applications,
1.	Broken Access Control
2.	Cryptographic Failures
3.	Injection
4.	Insecure Design
5.	Security Misconfiguration
6.	Vulnerable and Outdated Components
7.	Identification and Authentication Failures
8.	Software and Data Integrity Failures
9.	Security Logging and Monitoring Failures
10.	Server-Side Request Forgery (SSRF)


