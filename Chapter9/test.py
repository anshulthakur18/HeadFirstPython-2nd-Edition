import crypt

def verify_password(stored_hash, password):
    # Extract the salt and hashing algorithm identifier from the stored hash
    salt = '$'.join(stored_hash.split('$')[:3])
    
    # Hash the provided password with the extracted salt
    hashed_password = crypt.crypt(password, salt)
    
    # Compare the hashed password with the stored hash
    return hashed_password == stored_hash

# Example usage
stored_hash = "$6$ww2wM4KU$pJPPkhaMyYEBfy6Um4Wl7tfp9RAH3.zlC1lxrbkwcqd3BvdE05XFTI8xdEhnFtPLPp0mZlSRObRhWGQUOQ8T8/"  # Replace with actual hash from /etc/shadow
password = "R~AxfImNY8]nB06_1P*79B&wDP=5La0&"  # Replace with the password you want to verify

if verify_password(stored_hash, password):
    print("Password is correct.")
else:
    print("Password is incorrect.")
