import tkinter as tk
def readFile():
        filename  = name_entry.get()
        if filename:
            with open(filename + '.txt','r')as file:
                         data = file.read()
                         tampilentry.delete("1.0", tk.END)
                         tampilentry.insert(tk.END, data)
                         #file.write(data)
                
def create_file():
    filename = name_entry.get()
    if filename:
        with open(filename + '.txt', 'w') as file:
            data = teksentry.get("1.0", tk.END)
            file.write(data)
def append_data():
    name = name_entry.get()
    if name:
        with open('data.txt', 'a') as file:
            data = teksentry.get("1.0'",tk.END)
            file.write(data)
        
       
def hapus_data():
    filename = name_entry.get()
    if filename:
        with open(filename + '.txt', 'r') as file:
            lines = file.readlines()

        delete_text = fileentry.get()
        updated_lines = [line for line in lines if line.strip() != delete_text]

        with open(filename + '.txt', 'w') as file:
            file.writelines(updated_lines)
            


def update_file():
    file_name = name_entry.get()
    if file_name:
        with open(file_name + '.txt', 'r') as file:
            lines = file.readlines()
        search_text = searchentry.get("1.0",tk.END).strip()
        update_text = updateentry.get("1.0",tk.END).strip()
        updated_lines = [line.replace(search_text, update_text) for line in lines]

        with open(file_name + '.txt', 'w') as file:
            file.writelines(updated_lines)
    
root = tk.Tk()
root.title("Pengelolaan Data Txt")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
name = tk.Label(root, text="Nama:").grid(row=0, column=0)

teks = tk.Label(root,text= "Teks: ").grid(row=1,column=0)
teksentry=tk.Text(root,height=3,width=45)
teksentry.grid(row=1,column=1)
create = tk.Button(root, text = "Create",command=create_file).grid(row=1,column=2)
append = tk.Button(root,text="Append",command=append_data).grid(row=2,column=2)

tampil = tk.Label(root,text="Tampil: ")
tampil.grid(row=1,column=5)
tampilentry = tk.Text(root,height=3,width = 45)
tampilentry.grid(row=1,column=6)
read= tk.Button(root,text="Read",command=readFile).grid(row=1,column=7)

search= tk.Label(root,text="Search text: ").grid(row=3,column = 0)
searchentry=tk.Text(root,height=1,width=20)
searchentry.grid(row=4,column=0)

update_label=tk.Label(root,text="Update Text: ")
update_label.grid(row=3 ,column=2)
updateentry=tk.Text(root,height=1,width=20)
updateentry.grid(row=4,column=2)
updtbutton=tk.Button(root,text="Update",command=update_file)
updtbutton.grid(row=4,column=3)

file=tk.Label(root,text="File: ").grid(row=6,column=0)
fileentry=tk.Text(root,height=1,width = 20)
fileentry.grid(row=7,column=0)
filebutton=tk.Button(root,text="Delete",command =hapus_data).grid(row=7,column = 1)
root.mainloop()
