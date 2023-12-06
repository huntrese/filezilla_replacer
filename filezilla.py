from ftplib import FTP
import os
# Replace these with your FileZilla server credentials


def download_files(domain="",server = "",username = "",password = ""):
# Connect to the FileZilla server
    def download_index_php_from_folder(ftp, folder):
        # Navigate to the folder
        ftp.cwd(f'www/{domain}/{folder}')

        # Define the local file path to download to
        local_file_path = f"indexes/{folder}/index.php"  # Save each index.php with folder name as prefix
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        # Open a local file for writing in binary mode
        with open(local_file_path, 'wb') as local_file:
            # Retrieve the file from the server and write it to the local file
            ftp.retrbinary('RETR index.php', local_file.write)
        
        print(f"Downloaded index.php from {folder}")
        ftp.cwd("../../..")


    # Connect to the FileZilla server
    ftp = FTP(server)
    ftp.login(user=username, passwd=password)

    # Navigate to the 'talismanmd.ru' directory


    ftp.cwd(f'www/{domain}')



    # Get a list of directories inside 'talismanmd.ru'
    directories = ftp.nlst()[2:]
    print(directories)

    # Iterate through each directory and download index.php
    for folder in directories:
        try:
            download_index_php_from_folder(ftp, folder)
        except Exception as e:
            print(f"Error downloading index.php from {folder}: {e}")
            ftp.cwd("../../..")

    # Close the FTP connection
    ftp.quit()