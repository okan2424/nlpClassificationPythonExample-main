import io
import nltk
from nltk import pos_tag
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from nltk.corpus import stopwords
import re
import glob

class read:
    def __init__(self,yol):
        self.yol=yol
    def pdf2text(self):
        infile = open(self.yol, 'rb')
        resMgr = PDFResourceManager()
        retData = io.StringIO()
        TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
        interpreter = PDFPageInterpreter(resMgr, TxtConverter)

        for page in PDFPage.get_pages(infile):
            interpreter.process_page(page)
        txt = retData.getvalue()
        return txt

""" 
class temizle: # veri seti eğittik daha işimiz yok
    def __init__(self,yeniYol):
        self.yeniYol = yeniYol
        metın = self.yeniYol
        file = open("matveri.txt", "w+")
        for i in metın:
            file.write(i)
        metin = file.read()
        file.close()
        self.unicodCleaner(metin)
    def unicodCleaner(self,metin):
        kume = set()
        # Metindeki unicodları temizle
        text = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+://\S+)|^rt|http.+?", "", metin)
        # Metini Kelimelerine ayırıyoruz
        kelimeler=nltk.word_tokenize(text)
        # Kelimeleri etiketliyoruz
        # ve kelimeleri yeni bir txt dosyasının içine yazıyoruz.
        file2=open("mathCleanData.txt","w")
        tagget=pos_tag(kelimeler)
        # Etiketlediğimiz gelimelerin içinde özel isim olanları bir listeye atıyoruz
        özelisim= [i for i,pos in tagget if pos=='NNP']
        # Özelisim  kelimeleri bir kümeye atıyoruz nedeni ise kümede aynı elemanlar bulunumaz.
        # buda bizim veriyi daha doğru bir şekilde eğitmemiz için önemli
        kume.update(özelisim)

        for i in kume:
            file2.write(i+"\n")
        file2.close()
        self.kucultucu()
    def kucultucu(self):
        sw = set(stopwords.words('english'))
        file2=open("matveri.txt")
        oku3=file2.read()
        oku4=oku3.lower()
        kelimeler1=nltk.word_tokenize(oku4)
        filtre=[]
        for i in kelimeler1:
            if i not in sw:
                filtre.append(i)
        file2.close()
        file2=open("mathCleanData.txt","w+")

        for i in filtre:
            if len(i)>2:
                file2.write(i+"\n")
        bastir=file2.read()
        print(bastir)


"""



#temizle = temizle(oku.pdf2text())


class comparisonn:
    tip1 = open("tıp-veri-kümesi.txt")
    tip2 = tip1.read()
    tip = nltk.word_tokenize(tip2)

    tarih1 = open("tarih-veri-kümesi.txt")
    tarih2 = tarih1.read()
    tarih = nltk.word_tokenize(tarih2)

    matematik1 = open("matematik-veri-kümesi.txt")
    matematik2 = matematik1.read()
    matematik = nltk.word_tokenize(matematik2)

    path = input("Dosya adi Girin")
    read = read(path)
    kelimeler = nltk.word_tokenize(read.pdf2text())
    def __init__(self):
     self.byComparison()
    def byComparison(self):

        tipSayac=0
        tarihSayac=0
        matematikSayac=0

        for i in self.kelimeler:
              if(i in self.tip):
                  tipSayac = tipSayac + 1
              elif(i in self.tarih):
                  tarihSayac = tarihSayac + 1
              elif(i in self.matematik):
                  matematikSayac = matematikSayac + 1
        if(tipSayac>matematikSayac and tipSayac > tarihSayac):
            print(self.path+"Adlı Dosya Tıptır")
            return 0
        if (matematikSayac > tipSayac and matematikSayac > tarihSayac):
            print(self.path+"Adlı Dosya Matematiktir")
            return 0

        if (tarihSayac > matematikSayac and tarihSayac > tipSayac):
            print(self.path+"Adlı Dosya Tarihtir")
            return 0


comparisonn = comparisonn()
