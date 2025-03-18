from abc import ABC, abstractmethod


class FILE(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass

    def start_loading_file(self):
        product = self.load()
        final_product = product.download()
        return final_product

class EXCELFile(FILE):
    def load(self):
        return EXCEL()



class DOCFile(FILE):
    def load(self):
        return DOC()


class PDFFile(FILE):
    def load(self):
        return PDF()


class JPGFile(FILE):
    def load(self):
        return JPG()


class EXCEL:
    def download(self):
        return "excel Download Begin"

class DOC:
    def download(self):
        return "Document Download Begin"


class PDF:
    def download(self):
        return "PDF Download Begin"


class JPG:
    def download(self):
        return "JPG Download Begin"


def client(choice):
    format = {"pdf":PDFFile, "doc":DOCFile, "jpg":JPGFile , "excel":EXCELFile}
    result = format[choice.casefold()]()
    return result.start_loading_file()


choice = input("Enter export format for your file: ")
r = client(choice)
print(r)

