import sys
import os
import markdown # type: ignore
from markdown.extensions.tables import TableExtension # type: ignore

def main():

    converter = Converter()
    converter.execute()


# python file-converter.py markdown inputfile outputfile
class Converter():
    
    args = sys.argv

    def execute(self):

        validate = Validate()

        if validate.arg_check() != True:
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Error : Please enter the correct command and arguments!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        
        elif validate.cmd_check() != True:
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Error : This is not a correct command!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        
        elif validate.is_inputfile() != True:
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Error : Input file does not exist. Please try again!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        
        elif validate.is_outputfile() != True:
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Error : The same file name already exists. Please try again!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

        else:
            inputfile_path = self.args[2]
            outputfile_path = self.args[3]
            
            with open(inputfile_path) as f:
                contents = f.read()
        
            html = markdown.markdown(contents, extensions=['tables'])
            encode = "<meta charset=\"UTF-8\">\n"

            with open(outputfile_path, 'w', encoding="utf-8") as f:
                f.write(encode + html)

            print("\n --------------------- \n| You have succeeded! |\n ---------------------")
    
class Validate():

    args = sys.argv

    def arg_check(self):

        if (len(self.args) != 4):
            return False
        else:
            return True
        
    def cmd_check(self):
        cmd = self.args[1]
        if (cmd == "markdown"):
            return True
        else:
            return False
        
    def is_inputfile(self):

        inputpath = self.args[2]
        is_inputfile = os.path.isfile(inputpath)

        # 入力ファイルがなければやり直し
        if is_inputfile:
            return True
        else:
            return False
        
    def is_outputfile(self):

        outputpath = self.args[3]
        is_outputfile = os.path.isfile(outputpath)

        # すでに存在しているファイル名ならやり直し
        if is_outputfile:
            return False
        else:
            return True


main()