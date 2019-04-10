from django.db import connection
import os

def get_folderlocation():
    cursor = connection.cursor()
    cursor.execute("SELECT [PathLocation]FROM [dbo].[ConfigMaster] where [PathName] = 'FileShareLocation'")
    remotepath = cursor.fetchall()
    # print remotepath[0][0]
    return remotepath[0][0]

def folder_structure(CAFID, Clientid_name):
    folderpath = ''
    remotepath = get_folderlocation()
    clientdir = os.path.join(remotepath, '' + Clientid_name + '')
    if not os.path.exists(clientdir):
        os.mkdir(clientdir)
    CAFIDdir = os.path.join(clientdir, '' + CAFID + '')
    if not os.path.exists(CAFIDdir):
        os.mkdir(CAFIDdir)
    folderpath = (os.path.join(CAFIDdir))
    return (folderpath)

