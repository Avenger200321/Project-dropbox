import dropbox
import os
from dropbox import files 
from dropbox.files import WriteMode
class Automatic:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dxb=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files : 
                localpath=os.path.join(root, filename)
                relativepath = os.path.relpath(localpath, file_from)
                dropbox_path = os.path.join(file_to,relativepath)
                with open(localpath, 'rb' )as f : 
                    dxb.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

def main():
    access_token='sl.Av7KViPvq1G2IJ4GFKxDmhn63AKo5fHSSH1hEbql466pdE31NTiArSnTeJBKdAvTumXI6razvcyRDsjC1k1UJ0nhIO7YJNMG4loFj_s-pbpQDdKYY82qG4XackebIMb4E9eLqVI'
    autom = Automatic(access_token)
    file_from = 'Test.txt'
    file_to = '/Python Class 101/test.txt'
    autom.upload_file(file_from, file_to)
if __name__ == '__main__':
    main()