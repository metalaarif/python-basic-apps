class FileHandler:
    def readData(self, fileName):
        file1 = open(fileName, "r")
        content = file1.readlines()
        file1.close()
        return content

class FilterData(FileHandler):
    def readData(self, fileName):
        content = super().readData(fileName)
        datalist = []
        for line in content:
            if line.lower().startswith('k'):
                datalist.append(line.strip())
        return datalist

f1 = FilterData()
print(f1.readData("data.txt"))

print(FilterData.mro()) # method resolution order, to find how inheritance working