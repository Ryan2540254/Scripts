#!/usr/bin/env python3
import reportlab
from reportlab.platypus   import SimpleDocTemplate
from reportlab.platypus   import Paragraph, Spacer, Table, Image

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib        import colors

from reportlab.graphics.shapes           import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units                 import inch


styles = getSampleStyleSheet()

fruits = {'elderberries':1,
          'figs':1,
          'apples':2,
          'durians':3,
          'bananas':5,
          'cherries':8,
          'grapes':13 }


table_data = []
for k,v in fruits.items():
    table_data.append([k,v])

table_style = [('GRID',(0,0),(-1,-1),1,colors.black)]

report            = SimpleDocTemplate("/Users/ADMIN/Documents/report.pdf")
report_title      = Paragraph('A Complete Inventory of My Fruits.',styles['h1'])
report_table      = Table(data=table_data, style=table_style, hAlign='LEFT')

report_pie        = Pie(width=3*inch, height=3*inch)
report_pie.data   = []
report_pie.labels = []

report_chart      = Drawing()
report_chart.add(report_pie)

for fruit_name in sorted(fruits):
    report_pie.data.append(fruits[fruit_name])
    report_pie.labels.append(fruit_name)


report.build([report_title,report_table,report_chart])
