# 21 May 2025

# Remove the Computer Virus

# Your computer might have been infected by a virus! 
# Create a function that finds the viruses in files and removes them from your computer.
# Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
# Return "PC Files: Empty" if there are no files left on the computer.

def removeVirus(files: str) -> str:
    if not files.startswith("PC Files:"):
        return "Invalid input"

    files_list = files.replace("PC Files:", "").strip().split(",")
    clean_files = []

    for file in files_list:
        file = file.strip()
        if ("virus" in file or "malware" in file) and not ("antivirus" in file or "notvirus" in file):
            continue
        clean_files.append(file)

    return "PC Files: " + ", ".join(clean_files) if clean_files else "PC Files: Empty"

if __name__ == "__main__":
    print(removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
    # Expected: "PC Files: spotifysetup.exe, dog.jpg"
