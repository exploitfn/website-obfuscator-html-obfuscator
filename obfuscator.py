import os
import urllib.parse
import time

def obfuscate_html_file(file_path):
    with open(file_path, 'r') as file:
        html_code = file.read()

    obfuscated_html = urllib.parse.quote(html_code)

    with open(file_path, 'w') as file:
        file.write('<html><body><script>document.write(decodeURIComponent("{}"));</script></body></html>'.format(obfuscated_html))

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

    print("\n  [+] Obfuscated Files Successfully!")

current_directory = os.getcwd()
obfuscate_html_files_in_directory(current_directory)
