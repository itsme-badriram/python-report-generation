import pandas as pd

df = pd.read_csv('report.csv')
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "pdf.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(df=df)
html_file = open('result' + '.html', 'w')
html_file.write(outputText)
html_file.close()

import pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_file('result.html', 'result.pdf', configuration=config)
