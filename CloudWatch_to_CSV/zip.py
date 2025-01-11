import zipfile

# Files to include in the zip
files = ["csvconfig.py", "cwreport.py"]

# Create the zip file
with zipfile.ZipFile("lambda.zip", "w") as zipf:
    for file in files:
        zipf.write(file)

print("Files zipped successfully!")