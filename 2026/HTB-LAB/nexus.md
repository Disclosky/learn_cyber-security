nmap scan result:
  ```
  PORT   STATE SERVICE VERSION
  22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
  | ssh-hostkey: 
  |   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
  |_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
  80/tcp open  http    nginx 1.24.0 (Ubuntu)
  | http-methods: 
  |_  Supported Methods: GET HEAD POST OPTIONS
  |_http-server-header: nginx/1.24.0 (Ubuntu)
  |_http-title: Did not follow redirect to http://nexus.htb/
  Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
  ```

- try to explore the website, but only find `j.matthew@nexus.htb` 

- then I just try login to ssh using it, but I think guessing the password is not that easy

- try to enumerate subdomain and add filter to 302 code after some trying then found `git.nexus.htb`

- found `DB_PASSWORD=N27xh!!2ucY04` in admin/krayin-docker-setup/.env 

- `APP_URL=http://billing.nexus.htb`, then try to login using email j.matthew@nexus.htb. And I loged in..
refer to the CVE-2026-38526 it vulnerable to Remote Code Execution but I try to upload every endpoint I find, they didn't work.. I must upload in here`admin/tinymce/upload`. Maybe I give up here and read the writeups..


oh sometimes we can change the extension using intercept Burpsuite

`systemctl list-timers` I don't know how it works,.. and I'm not be able to obtain root flag right now. I will comeback later..

yup, I figure it out why it's not work for me. It's need me to generate an SSH key pair **locally**.

[Nexus](https://labs.hackthebox.com/achievement/machine/2139280/948)
