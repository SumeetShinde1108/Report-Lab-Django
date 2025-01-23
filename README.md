# Report Lab Installation 
## For free version (Report Lab PDF Toolkit)
```shell
pip install reportlab
```
### Feature libraries and tools =  
1) Preppy : ReportLab's Preppy is a lightweight, templating engine designed to generate dynamic content for PDF reports.
2) PyRXP : PyRXP is a high-performance, validating XML parser and writer for Python, developed by ReportLab. It offers fast processing of XML data with support for namespaces and efficient handling of large documents.
## For paid version (Report Lab PLUS)
#### Step 1) Visit the report lab website, purchase the Report Lab PLUS license. You will recieve credentials and access the private PyPI server.
#### Step 2) Create pip confuguation file, open notepad as administrator and create file as a %APPDATA%\pip\pip.conf
```
[global]
extra-index-url:https://username:password@plus.reportlab.com/pypi/
```
#### step 3) Then install ReportLab PLUS by using pip
```
pip install reportlab-plus 
```
### Feature libraries and tools =
1) Diagra : Simplifies the creation of flowcharts, network diagrams, and other visual representations. It integrates seamlessly with ReportLab's PDF generation tools for embedding diagrams in reports.
2) PageCatcher : A tool for modifying and reusing existing PDF content by adding overlays or annotations.
3) PDF Accessibility : Ensures PDFs are readable by assistive technologies, supporting standards like PDF/UA.
4) json2pdf : Converts JSON data into formatted PDFs, dynamically mapping fields to layouts.
