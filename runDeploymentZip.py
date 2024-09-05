import os
import zipfile

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname)


folder_path = r'C:\Users\timde\Documents\CodeVault\PythonProjects\NBA_playwright\NBA-DJango_api\nba_stats_api'
zip_path = r'C:\Users\timde\Documents\CodeVault\PythonProjects\NBA_playwright\NBA-DJango_api\nba_stats_api\deployment.zip'

zip_folder(folder_path, zip_path)
