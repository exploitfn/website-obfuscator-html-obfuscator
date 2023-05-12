import os
import base64
import time

os.system("pip install bs4")

# made my ud man
def obfuscate_html_file(file_path):
    with open(file_path, 'r') as file:
        html_code = file.read()

    obfuscated_html = base64.b64encode(html_code.encode()).decode()

    with open(file_path, 'w') as file:
        file.write('<script>document.documentElement.innerHTML = atob("{}");</script>'.format(obfuscated_html))

def obfuscate_html_files_in_directory(directory):
    total_files = 0
    processed_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                total_files += 1

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                obfuscate_html_file(file_path)
                processed_files += 1
                percent_done = int((processed_files / total_files) * 100)
                print("\r  [+] Obfuscating HTML Files: {}% done.".format(percent_done), end="")
                time.sleep(0.5)

    print("\n  [+] Obfuscated Files Successfully !!")

current_directory = os.getcwd()

obfuscate_html_files_in_directory(current_directory)
