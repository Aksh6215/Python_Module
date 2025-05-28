import re
import threading

pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$')

valid_password_file = 'valid_passwords.txt'
invalid_password_file = 'invalid_passwords.log'

file_lock = threading.Lock()

def validate_password(password):
    if pattern.match(password):
        return True, None
    else:
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', password):
            errors.append("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            errors.append("Password must contain at least one lowercase letter")
        if not re.search(r'\d', password):
            errors.append("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain at least one special character")
        return False, errors

def log_valid_password(password):
    with file_lock:
        with open(valid_password_file, 'a') as f:
            f.write(password + '\n')

def log_invalid_password(password, errors):
    with file_lock:
        with open(invalid_password_file, 'a') as f:
            f.write(f"Invalid Password: {password} | Errors: {', '.join(errors)}\n")

def process_password(password):
    is_valid, errors = validate_password(password)
    if is_valid:
        log_valid_password(password)
        print(f"Valid Password: {password}")
    else:
        log_invalid_password(password, errors)
        print(f"Invalid Password: {password} | Errors: {', '.join(errors)}")

passwords = input("Enter passwords : ").split()

threads = []
for password in passwords:
    thread = threading.Thread(target=process_password, args=(password,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Password validation complete! Check valid_passwords.txt & invalid_passwords.log.")
