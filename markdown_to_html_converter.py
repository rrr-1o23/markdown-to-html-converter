import sys
import markdown # type: ignore
from markdown.extensions.tables import TableExtension # type: ignore

def main():
    
    commands = sys.argv
    print("\n", commands)

    converter(commands)


# マークダウンからHTMLに変換
def converter(commands):

    command = commands[1]
    inputfile_path = commands[2]
    outputfile_path = commands[3]

    with open(inputfile_path) as f:
        contents = f.read()
    
    html = markdown.markdown(contents, extensions=['tables'])
    encode = "<meta charset=\"UTF-8\">\n"

    with open(outputfile_path, 'w', encoding="utf-8") as f:
        f.write(encode + html)

    

main()