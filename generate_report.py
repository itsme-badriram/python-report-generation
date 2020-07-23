import pandas as pd

#Read the cs file
df = pd.read_csv('report.csv')
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
#HTML template I use is 'pdf.html'
TEMPLATE_FILE = "pdf.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(df=df)
html_file = open('result' + '.html', 'w')
html_file.write(outputText)
html_file.close()
#Convert the HTML file(result.html) generated to PDF.
import pdfkit
#This configuration is not required if the required modules are added to the path as environment variables.
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_file('result.html', 'result.pdf', configuration=config)
