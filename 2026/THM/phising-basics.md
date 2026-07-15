## PHISING BASICS 

Even the most secure organisations rely on people, people can be tricked, manipulated, and persuaded into giving up access.

A single well-crafted email can bypass technical controls, plant malware, or steal credentials that unlock the door to your target’s network. 

Learning Objectives:
   - What phising is and its role in a pentest 
   - The psychology behind phising
   - Common phising attacks
   - The anatomy of a phising campaign
   - Phising tools

---
### Wednesday, 15 July 2026

Phising is a form of cyber attack that uses social engineering to trick people into revealing sensitive information or running malware on their devices. by impersonating legitimate sources via emails, text messages, phone calls, or fake websites.

The primary channels for attacks include email, SMS (known as smishing), voice calls (vishing), and fake websites designed to look legitimate. 

#### Type of Phising:
   - **`Phising`**  is the scam's broad, "cast a wide net" version.
   - **`Spear Phising`** is a targeted attack tailored to a specific person.
   - **`Whaling`** is spear phising that targets senior decision-makers and executives, like CEOs and CFOs.

---
#### URL and Domain Manipulation
   - **`URL Masking:`** Involves disguising a malicious URL behind a legitimate-looking hyperlink. 
   - **`Homograph Attacks:`** Exploit visual similarities between domain name characters, for example, replacing "o" with "0" or using Cyrillic characters.
   - **`Typosquatting:`** Involves registering domains similar to legitimate ones, relying on users making typing errors.

>Attackers can use URL shorteners to hide a link's true destination. These URLs are more complicated for users to inspect and can bypass basic security checks.

#### Email Spoofing

If a domain is lacking security measures for authentication, an attacker can use a Python script to modify their email address. This is possible because **SMTP** (Simple Mail Transfer Protocol) does not have built-in functionality for authenticating email addresses.

Many organisations use security measures, such as **SPF**(Sender Policy Framework), **DMARC**(Domain-based Message Authentication, Reporting, and Conformance), and **DKIM**(DomainKeys Identified Mail ), to help prevent such attacks. 

#### Some popular tools:
   - [GoPhish](https://github.com/gophish/gophish)
   - [EvilNginx ](https://github.com/kgretzky/evilginx2)
   - [The Social Engineering Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)

---
#### Ethical Phishing in Pentesting

Conducting a phishing test without a formal agreement is illegal. Ethical hackers must strictly follow a authorized legal framework to protect both parties.

**1. The Legal Agreement (Must-Haves)**

   - Scope of Work (SOW): Defines target employees, authorized methods, and campaign timelines.
   - Rules of Engagement (ROE): Outlines strict boundaries and safety protocols.
   - Whitelisting: IT teams pre-approve the test emails so they bypass spam filters to measure human behavior accurately.

**2. Step-by-Step Execution**

   1. Reconnaissance: Use only public information to make lures feel plausible without crossing privacy lines.
   2. Setup: Buying look-alike domains and configuring safe email servers.
   3. Launch: Sending realistic emails via tools like Gophish.
   4. Data Collection: Tracking clicks safely. Plaintext  passwords are never stored or collected.
   5. Education: Redirecting clicked users to a safe landing page explaining the drill.
   6. Reporting: Presenting statistics and security recommendations to management.



---
[TryHackMe | Phising Basics](https://tryhackme.com/room/phishingbasics)