# ꧁꧂  Batch Convert HTML files to PDF files

This tool is handy for automating batch HTML-to-PDF conversions, especially when handling large sets of files.

This script converts all .html files in a user-specified directory into .pdf format, simulating the behavior of printing the web pages from a browser. It uses wkhtmltopdf and the pdfkit library for this conversion process.


# ꧁꧂  How to run

### INSTALLATION:

Ensure that  wkhtmltopdf are installed on your system. You can install pdfkit via pip:

`pip install pdfkit`

Also, download and install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) from its official website and ensure it's added to your system's PATH or provide its path in the script.



Everyone must complete the steps above.

There are two different methods to run the script. Your preferance. 

### Method A.


`git clone https://github.com/noarche/html2pdf`

`pip install pdfkit`

`python html2pdf.py`


### Method B.

After cloning the repo you will need to extract the .exe from the archive which have been split into parts located inside ./Windows-Portable-Exe/

Download [Winrar](https://www.rarlab.com/download.htm) & install

Click `./Windows-Portable-Exe/html2pdf-windows-portable.part01` to start the extraction. Extract anywhere on your computer.

Double click the extracted `html2pdf.exe` file to run the script. 




### When you run the script, it will prompt you to enter the path to the directory containing .html files. The script will convert each .html file in that directory to a .pdf with the same name. The .pdf files will be located in the same directory as the .html files. 

-------------------------------------------------------------------

## 🛡️ Is this a virus❔

No it is not a virus, that is a false positive. Anything compiled with pyinstaller will be flagged as potentially malicious. Pyinstaller is what turns the .py file into a .exe file and allows people to run python scripts as portable applications without the need to install python or any dependancies.  

Please scan the actual source, the file that ends with '.py' -  It will with no doubt be 100% clean on virustotal.  That being said I have provided instructions on how to build your own exe from the file you know is clean. 


🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻

🛡️ Tip for all questionable applications: 

*Running the application via [Sandboxie](https://sandboxie-plus.com/downloads/) or similar app will virutalize and protect your OS as if it was running on a virtual machine - [Sandboxie](https://sandboxie-plus.com/downloads/) can be used with any application or installation package thus another great tool to have.* 

🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺

## ꧁꧂ ✨ How to Compile your own .exe file❔ 

*You are able to build your own exe file from the source on a windows and linux machine. Follow the steps below, assuming you have already installed pip*


Change to the directory containing the Python script
  	
    cd \html2pdf\

Run the following command to use pyinstaller to build an executable from the souce. Verify your version # in command matchs the version in source  dir. 
     
     pyinstaller --onefile html2pdf.py

Pyinstaller will created a couple of directories and files. 

    The .exe you want is located in \dist\html2pdf.exe



-------------------------------------------------------------------

# ꧁꧂  Buy me a coffee ☕

![qrCode](https://raw.githubusercontent.com/noarche/cd-ripper/main/unrelated-ignore/CryptoQRcodes.png)

**Bitcoin** address `bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j`


**Ethereum** address `0x94FcBab18E4c0b2FAf5050c0c11E056893134266`


**Litecoin** address `ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx`



-------------------------------------------------------------------

![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)

# Looking for a RSS Reader?

Check out my simple but powerful rss reader that comes with over 50 preconfigured RSS feeds! 

https://github.com/noarche/rss
