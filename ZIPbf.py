from tqdm import tqdm
import zipfile


x =""
wordlist = [passwords.strip() for passwords in open("passlist.txt")]
zip_file = zipfile.ZipFile("demo2.zip")

for i in tqdm(wordlist, desc="Checking password in wordlist"):
    try:
        zip_file.extractall(pwd=i.encode())
        x=i
        break
    except:
        continue
print("Password found: ", i)
