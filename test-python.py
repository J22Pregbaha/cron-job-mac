import datetime

now = datetime.datetime.now()
my_file = open("test.txt", "a")
my_file.write("Tis a weekday" + now.strftime("%A %d-%m-%Y %I:%M %p") + "\n")
my_file.close()
