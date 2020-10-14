"""Prépare les répertoires de travail et télécharge puis extrait le dataset demandé
"""

import requests
import sys
import os
import zipfile

class downloader():
    """Télécharge et extrait le fichier, pour plusieur répertoires :
    créer plusieures instances
    """
    def __init__(self, data_path):
        """Initialisation de l'objet et création ds répertoires de travail

        Args:
            data_path (str): chemin relatif vers le dossier qui accueillera les données 
        """
        self.data_path = data_path
        if not os.path.exists(self.data_path + f"/CURATED"):
            os.makedirs(self.data_path + f"/CURATED")
        if not os.path.exists(self.data_path + f"/RAW"):
            os.makedirs(self.data_path + f"/RAW")
        if not os.path.exists(self.data_path + f"/OUTPUT"):
            os.makedirs(self.data_path + f"/OUTPUT")

    def data_download(self, file_name, download_url):
        """Téléchargement du fichier

        Args:
            file_name (str): Nom du fichier une fois téléchargé
            download_url (str): URL permettant le téléchargement du fichier
        """
        print('Data downloading...')
        with open(self.data_path + "/RAW/" + file_name, "wb") as file:
            response = requests.get(download_url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                file.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    file.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('■' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()

        print('Download finished')

    def data_extract(self, file_name):
        """Extraction du fichier

        Args:
            file_name (str): Nom du fichier a extraire
        """
        print("Data extracting...")
        with open(self.data_path + "/RAW/" + file_name, 'r') as zipObj:
            zipObj.extractall(self.data_path + "/RAW")
        print("Extraction complete")
