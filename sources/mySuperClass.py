#!/usr/bin/env python3

class mySuperClass():
        
        # return True
        def functionTrue(self):
                return True
        
        # lit les fichiers dont le nom est passe en argument
        # return True dans le cas 'normal', False en cas d'erreur
        def functionReadFile(self, filename='main', display=False):
                try:
                        myFile = open(filename, 'r')
                        print('Read file OK')
                        if display:
                                print(myFile.read())
                        myFile.close()
                        return True
                except:
                        print('Error, cannot open file', filename)
                        return False
