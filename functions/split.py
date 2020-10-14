"""Permet de splitter les fichiers csv,tsv etc.
"""

import csv
import os

class Splitter:
    """Splitter de fichiers, en cas de nombreux types de fichiers avec différents délimiteurs :
    créer plusieurs instances
    """
    def __init__(self, data_folder, delimiter):
        """Initialisation de l'objet

        Args:
            data_folder (str): chemin relatif vers le dossier contenant les données
            delimiter (str): delimiter des fichiers a traiter
        """
        self.data_path = data_folder
        self.delimiter = delimiter
        if not os.path.exists(f"{self.data_path}/CURATED"):
            os.makedirs(f"{self.data_path}/CURATED")
        if not os.path.exists(f"{self.data_path}/RAW"):
            os.makedirs(f"{self.data_path}/RAW")
        if not os.path.exists(f"{self.data_path}/OUTPUT"):
            os.makedirs(f"{self.data_path}/OUTPUT")

    def file_splitter(self, file_name, column_to_split_on, output_folder):
        """Splitter de fichiers

        Args:
            file_name (str): nom du fichier à traiter (avec le .csv, .tsv, .txt etc.)
            column_to_split_on (str ou int): nom de la colonne a partir de laquelle il faut créer les splits
            output_folder (str): nom du fichier dans lequel placer les fichiers splittés
        """
        csv.field_size_limit(10000000)
        with open(f"{self.data_path}/RAW/{file_name}", encoding='utf-8') as file:
            file_dict = csv.DictReader(file, delimiter=self.delimiter)

            already_opened_files = {}

            for row in file_dict:
                file_column = row[column_to_split_on]
                file_column = file_column.replace('\\', '.')
                file_column = file_column.replace('/', '.')

                if file_column not in already_opened_files:
                    out_file = open(f"{self.data_path}/CURATED/{output_folder}/{file_column}.csv",
                                    'w', encoding='utf-8')
                    dict_writer = csv.DictWriter(out_file, fieldnames=file_dict.fieldnames)
                    dict_writer.writeheader()
                    already_opened_files[file_column] = out_file, dict_writer

                already_opened_files[file_column][1].writerow(row)

            for output, _ in already_opened_files.values():
                output.close()

        print(f"Split fichier {file_name} terminé")
