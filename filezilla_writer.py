from ftplib import FTP
import os
# Replace these with your FileZilla server credentials

def upload_files(domain="",server = '91.236.136.179',username = 'u799305_damian',password = 'rR4pN2zL3c'):
    # Connect to the FileZilla server
    def upload_index_php_from_folder(ftp, folder):
        # Navigate to the folder
        ftp.cwd(f'www/{domain}/{folder}')

        # Define the local file path to download to
        local_file_path = f"updated_indexes/{folder}/index.php"  # Save each index.php with folder name as prefix

        # Open a local file for writing in binary mode
        with open(local_file_path, 'rb') as local_file:
            # Retrieve the file from the server and write it to the local file
            ftp.storbinary('STOR index.php', local_file)

        
        print(f"uploaded index.php from {local_file_path} to {folder}")
        ftp.cwd("../../..")


    # Connect to the FileZilla server
    ftp = FTP(server)
    ftp.login(user=username, passwd=password)

    # Navigate to the 'talismanmd.ru' directory


    ftp.cwd(f'www/{domain}')



    # Get a list of directories inside 'talismanmd.ru'
    for dirpath, dirnames, filenames in os.walk('indexes'):
        for folder in dirnames:
            try:
                upload_index_php_from_folder(ftp, folder)
            except Exception as e:
                print(f"Error uploading index.php from {folder}: {e}")
                ftp.cwd("../../..")

    # Close the FTP connection
    ftp.quit()