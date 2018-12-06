import webbrowser, os

file1 = open("index.html", "w")
file1.write('''
<html>
    <head>
        <title>HTML in Python</title>
    </head>
        <body>
        <h1> Employee Data </h1>
        <table border='1' width='50%' align='left' bgcolor="333FFF">
            <tr>
                <th>ID</th>
                <th>Name</th>
            </tr>
            <tr>
                <td>1001</td>
                <td>Aarif</td>
            </tr>
             <tr>
                <td>1002</td>
                <td>Metal</td>
            </tr>
        </table>
    </body>
</html>
''')
file1.close()
webbrowser.open("file://"+os.path.realpath("index.html"))