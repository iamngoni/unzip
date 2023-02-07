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
    for f in folders:
        try:
            logger.info('Moving files from folder: {}'.format(f))
            files = [f for f in os.listdir(f) if os.path.isfile(f)]
            for file in files:
                file_abspath = os.path.abspath(file)
                logger.info('Absolute path: {}'.format(file_abspath))
                os.rename(file_abspath, os.path.join(os.path.abspath('.'), file))
            logger.info('Deleting folder: {}'.format(f))
            os.rmdir(f)
            logger.info('----------------------------------------')
        except Exception as exc:
            logger.error('Error moving files from folder: {}'.format(f))
            logger.error(exc)
            logger.error('------------------Skipping----------------------')

if __name__ == '__main__':
    unzip()
