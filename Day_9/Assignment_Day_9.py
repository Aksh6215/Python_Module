'''
Problem Statement: Multi-Threaded Password Validator
Objective:
Design a multi-threaded password validator that checks multiple passwords concurrently and
stores them securely.
Requirements:
1) Password Validation Using Regex:
 A password must meet the following criteria:
o At least 8 characters long
o Contains at least one uppercase letter
o Contains at least one lowercase letter
o Contains at least one digit
o Contains at least one special character (!@#$%^&amp;*(),.?&quot;:{}|&lt;&gt;)

2️) Multi-Threading for Performance:
 Use Python’s threading module to validate multiple passwords simultaneously.
3️) File Handling for Secure Storage:
 Valid passwords should be stored in valid_passwords.txt.
 Invalid passwords along with reasons for rejection should be logged in
invalid_passwords.log.
4️) Exception Handling for Errors:
 Handle potential errors related to:
o File read/write operations
o Incorrect input formats
o Thread execution issues

Example Input &amp; Output
Input:
�� Enter passwords separated by space: Pass@123 weakpass P@ssword123 Abc!123
Output:
Valid Password: Pass@123
Invalid Password: weakpass | Errors: Password must be at least 8 characters long, Password must
contain at least one uppercase letter, Password must contain at least one digit, Password must
contain at least one special character

Valid Password: P@ssword123
Invalid Password: Abc!123 | Errors: Password must be at least 8 characters long, Password must
contain at least one digit
Password validation complete! Check valid_passwords.txt &amp; invalid_passwords.log.

�� Constraints:
 The program should handle multiple passwords concurrently using multi-threading.
 The validation must be fast and efficient, even for 100+ passwords.
 Log files should store invalid attempts for future reference.
'''

class password_validator:
    def __init__(self):
        