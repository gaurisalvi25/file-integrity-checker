import hashlib
import os
import json
from datetime import datetime

# File to store original hashes
HASH_STORE_FILE = "file_hashes.json"

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def store_initial_hashes(directory):
    """Store initial file hashes in a JSON file."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = calculate_hash(path)
            if file_hash:
                hashes[path] = {
                    "hash": file_hash,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

    with open(HASH_STORE_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"[+] Initial file hashes stored in '{HASH_STORE_FILE}'.")

def check_file_integrity():
    """Check current file hashes against stored ones."""
    try:
        with open(HASH_STORE_FILE, "r") as f:
            old_hashes = json.load(f)
    except FileNotFoundError:
        print("[!] No stored hashes found. Please run initial scan first.")
        return

    changes_detected = False

    for file_path, data in old_hashes.items():
        old_hash = data["hash"]
        current_hash = calculate_hash(file_path)
        if current_hash is None:
            print(f"[-] File missing: {file_path}")
            changes_detected = True
        elif current_hash != old_hash:
            print(f"[!] File changed: {file_path}")
            changes_detected = True
        else:
            print(f"[OK] File unchanged: {file_path}")

    if not changes_detected:
        print("[+] All files are intact.")

if __name__ == "__main__":
    print("=== File Integrity Checker ===")
    print("1. Store initial hashes (first-time setup)")
    print("2. Check file integrity")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        folder = input("Enter folder path to monitor: ")
        if os.path.exists(folder):
            store_initial_hashes(folder)
        else:
            print("[!] Folder does not exist.")
    elif choice == "2":
        check_file_integrity()
    else:
        print("Invalid choice.")
