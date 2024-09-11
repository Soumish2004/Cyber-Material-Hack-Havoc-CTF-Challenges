import requests
import os

def directory_busting(url, wordlist_path):
    # Check if the wordlist file exists
    if not os.path.isfile(wordlist_path):
        print(f"Wordlist file {wordlist_path} not found.")
        return
    
    # Open the wordlist file
    with open(wordlist_path, "r") as wordlist:
        for word in wordlist:
            # Clean up the word (remove any extra whitespace or newlines)
            word = word.strip()
            
            # Construct the full URL to test
            full_url = f"{url}/{word}"
            
            try:
                # Send a GET request to the URL
                response = requests.get(full_url)
                
                # If the response status code is 200, the directory/file exists
                if response.status_code == 200:
                    print(f"[+] Found: {full_url}")
                elif response.status_code == 403:
                    print(f"[!] Forbidden: {full_url}")
                elif response.status_code == 301 or response.status_code == 302:
                    print(f"[~] Redirected: {full_url}")
                
            except requests.exceptions.RequestException as e:
                print(f"Error connecting to {full_url}: {e}")

if __name__ == "__main__":
    # Set the target URL and wordlist file path
    target_url = "http://challenge.ctf.cybermaterial.com/challenge1/"  # Replace with the target URL
    wordlist_file = "E:\hack havoc\Writeups\Web\A Shakespearian Tragedy\common.txt"  # Replace with the path to your wordlist
    
    print(f"Starting directory busting on {target_url} with wordlist {wordlist_file}...")
    directory_busting(target_url, wordlist_file)
