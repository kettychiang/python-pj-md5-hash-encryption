import hashlib

# Set two variables for both strings
string_a = "Victoria University"
string_b = "22603VIC - Certificate IV in Cyber Security"

# Generate MD5 hash for string_a
hash_a = hashlib.md5(string_a.encode()).hexdigest()
print("MD5 hash of 'Victoria University':", hash_a)

# Generate MD5 hash for string_b
hash_b = hashlib.md5(string_b.encode()).hexdigest()
print("MD5 hash of '22603VIC - Certificate IV in Cyber Security':", hash_b)