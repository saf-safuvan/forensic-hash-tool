import hashlib
import time
import os

def generate_hashes(file_path):

    algorithms = {
        "MD5": hashlib.md5(),
        "SHA1": hashlib.sha1(),
        "SHA256": hashlib.sha256(),
        "SHA384": hashlib.sha384(),
        "SHA512": hashlib.sha512()
    }

    start_time = time.time()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            for algo in algorithms.values():
                algo.update(chunk)

    end_time = time.time()

    print("\nGenerated Hash Values:\n")

    for name, algo in algorithms.items():
        print(f"{name} : {algo.hexdigest()}")

    print("\nTime taken:", round(end_time - start_time, 4), "seconds")


def verify_hash(file_path, expected_hash):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    calculated_hash = sha256.hexdigest()

    if calculated_hash == expected_hash:
        print("✅ File integrity verified")
    else:
        print("❌ File has been modified")


if __name__ == "__main__":

    print("==== Digital Forensics Hash Tool ====")

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("File not found")
        exit()

    generate_hashes(file_path)

    choice = input("\nDo you want to verify file integrity? (y/n): ")

    if choice.lower() == "y":
        expected_hash = input("Enter expected SHA256 hash: ")
        verify_hash(file_path, expected_hash)
