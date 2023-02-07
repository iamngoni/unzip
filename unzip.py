#
# unzip.py
# unzip
#
# Created by Ngonidzashe Mangudya on 8/2/2023.

import zipfile
import sys
from loguru import logger
import os

# scan all zipped files in working directory and unzip files into the same directory
def unzip():
    files = [f for f in os.listdir('.') if f.endswith('.zip')]
    logger.info('Preparing to unzip {} files.'.format(len(files)))
    logger.info('----------------------------------------')
    for f in files:
        try:
            file_abspath = os.path.abspath(f)
            logger.info('Absolute path: {}'.format(file_abspath))
            with zipfile.ZipFile(file_abspath, 'r') as zip_ref:
                logger.info('Unzipping file: {}'.format(f))
                zip_ref.extractall('.')
                zip_ref.close()

            # delete zip file
            os.remove(file_abspath)
            logger.info('Deleted zip file: {}'.format(f))
            logger.info('----------------------------------------')

        except Exception as exc:
            logger.error('Error unzipping file: {}'.format(f))
            logger.error(exc)
            logger.error('------------------Skipping----------------------')


    # check if any folders were extracted and move files to the parent dir
    folders = [f for f in os.listdir('.') if os.path.isdir(f)]
    logger.info('Preparing to move files from {} folders.'.format(len(folders)))
    logger.info('----------------------------------------')
    for folder in folders:
        try:
            logger.info('Moving files from folder: {}'.format(folder))
            # get directory full path
            folder_abs_path = os.path.abspath(folder)
            logger.info('Absolute path: {}'.format(folder_abs_path))
            files = [anime_file for anime_file in os.listdir(folder_abs_path) if os.path.isfile(os.path.join(folder_abs_path, anime_file))]
            logger.info('Found {} files.'.format(len(files)))
            for anime_file in files:
                file_abspath = os.path.join(folder_abs_path, anime_file)

                # check if absolute path exists
                if os.path.exists(file_abspath):
                    pass
                else:
                    raise Exception('File does not exist. Moving cannot continue.')

                logger.info('Absolute path: {}'.format(file_abspath))
                os.rename(file_abspath, os.path.join(os.path.abspath('.'), anime_file))

            logger.info('Deleting folder: {}'.format(folder))
            os.rmdir(folder_abs_path)
            logger.info('----------------------------------------')
        except Exception as exc:
            logger.error('Error moving file "{}" from folder: {}'.format(anime_file, folder))
            logger.error(exc)
            logger.error('------------------Skipping----------------------')

if __name__ == '__main__':
    unzip()
