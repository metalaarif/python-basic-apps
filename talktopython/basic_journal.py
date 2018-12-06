#!/usr/bin/python3
# Creating a basic journal app where user can add new entries and then list them.
def main():
    header()
    file_structure()

def header():
    print("-" * 50)
    print("\t \t \t PERSONAL JOURNAL APP")
    print("-" * 50)

def file_structure():
    a = None
    journal_list = []

    while a != "x":
        a = input("What do you want to do with your Journal? \n[L]ist, [A]dd, E[x]it: ")
        a = a.lower().strip()

        if a == "l":
            list_entries(journal_list)
        elif a == "a":
            add_entries(journal_list)
        elif a != "x":
            print("Opps Error, Can't understand '%s' \n" %(a))

    print("\nThanks for Using! GoodBye")

def list_entries(info):
    entries = reversed(info)
    for index, stored_data in enumerate(entries):
        print("%s. %s" %(index + 1, stored_data))

def add_entries(info):
    raw_data = input("Journal entry..<enter> to exit:  ")
    info.append(raw_data)

main()