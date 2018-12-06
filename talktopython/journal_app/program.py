#!/usr/bin/python3
import journal_load_save as journal

def main():
    header()
    run_event_loop()
def header():
    print("-" * 50)
    print("\t Journal App")
    print("-" * 50)

def run_event_loop():
    cmd = "Empty"
    print("What do you want to do with your Journal? ")
    journal_name = "default"
    journal_data = journal.load(journal_name)

    while cmd != "x" and cmd:   # and cmd is defined for empty if user just press enter without typing anything
        cmd = input("[L]ist, [A]dd or E[x]it: ")
        cmd = cmd.lower().strip()
        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Error can't understand '%s' "%(cmd))
    print("Bye")
    journal.save(journal_name, journal_data)

def add_entry(data):
    text = input("Type entry <enter> to exit: ")
    journal.add_entry(text, data)

def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("[%d] %s"%(idx + 1, entry))

#print("filename ==>",__file__)
#print("name ==>", __name__)
if __name__ == "__main__":
    main()
