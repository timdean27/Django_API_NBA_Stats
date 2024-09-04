import os
import zipfile

def zip_folder(folder_path, zip_path):
    # Ensure zip_path ends with .zip
    if not zip_path.endswith('.zip'):
        zip_path += '.zip'

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                           os.path.join(folder_path, '..')))

folder_path = r'C:\Users\timde\Documents\CodeVault\PythonProjects\NBA_playwright\NBA-DJango_api\nba_stats_api'
zip_path = r'C:\Users\timde\Documents\CodeVault\PythonProjects\NBA_playwright\NBA-DJango_api\nba_stats_api\deployment.zip'

zip_folder(folder_path, zip_path)
