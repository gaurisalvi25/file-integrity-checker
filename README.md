# 🛡️ FILE INTEGRITY CHECKER

A **Python-based File Integrity Checker** that uses SHA-256 hashing to detect if files have been modified, deleted, or newly created.  
Perfect for monitoring critical files for changes — useful in cybersecurity, system administration, and compliance tasks.

---

## 📜 Features
- Generate SHA-256 hashes for files.
- Store hashes in a JSON database.
- Detect:
- **Modified files** (hash changed)
- **Deleted files** (file missing)
- **New files** (not in database)
- Easy to run and modify.

---

## 🚀 How It Works
1. **First run** → Generates hashes for all files in a folder and stores them.
2. **Next runs** → Compares current hashes with stored ones.
3. **Reports** any modifications, deletions, or new files.

---

## 🖥️ Installation & Usage
###1️⃣ Clone this repository:
```bash
git clone https://github.com/gaurisalvi25/file-integrity-checker.git
cd file-integrity-checker

###2️⃣ Install Python (if not already installed):
Download Python (version 3.8+ recommended)

###3️⃣ Run the script:
python file_integrity_checker.py

⚙️ Configuration
By default, the script scans the current working directory.

You can modify the folder path in the code:
FOLDER_TO_MONITOR = "path/to/your/folder"

📂 Files in this Repo
File	Description
file_integrity_checker.py	Main Python script
hashes.json	Stores the file hashes (auto-created)

💡 Future Improvements
Add email or Slack alerts.

Create a real-time monitoring mode.

Add a GUI version.

👩‍💻 Author
Gauri Salvi
💼 GitHub: gaurisalvi25

