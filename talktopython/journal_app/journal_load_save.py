import os

def load(name):
    '''
    This method creates and loads a new journal
    :param name: This base name of the journal to load
    :return: A new Journal data structure populated with the file data
    '''
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    filename = get_full_pathname(name)
    print(".....SAVING TO.....: %s \nSUCCESSFULLY SAVED"%(filename))

    with open(filename, "w") as fout:
        for entry in journal_data:
            fout.write(entry + "\n")

    # fout = open(filename, "w")
    # for entry in journal_data:
    #     fout.write(entry + "\n")
    # fout.close()


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", "journal", name + ".arf"))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)