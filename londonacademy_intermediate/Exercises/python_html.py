#!/usr/bin/python3
import os

html = open("index.html", "w+")
html.write('''
    <html>
    <head>
    <title>HTML via Python</title>
    </head>
    <body><h1>Hello, This is how python is embedded in an html file</h1></body
    </html>
''')
html.close()

table = open("table.html", "w+")
table.write('''
    <html>
    <head>
    <title>HTML via Python</title>
    </head>
    <body><h1 align="center">Table in Python</h1>
    <table border="1", bgcolor="Grey", align="center", width="500">
        <tr>
            <th>Employee</th>
            <th>Salary</th>
        </tr>
        <tr>
            <td>Tom</td>
            <td>25000</td>
        </tr>
        <tr>
            <td>Michael</td>
            <td>35000</td>
        </tr>
        <tr>
            <td>Lisa</td>
            <td>15000</td>
        </tr>
    </table>
    </body
    </html>
''')
table.close()