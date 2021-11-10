import os
import time
from tkinter import *
from tkinter import filedialog, messagebox, ttk 
import requests
import simplejson as json
import webbrowser

#|---Verificaçao da versao ---|
version="1.0.1"
def versao():
    url="https://api.github.com/repos/immlima/Tutorando/releases/latest"
    v = requests.get(url)

    if v.status_code == requests.codes.OK:
        git_info=json.loads(v.text)
        if version!=str(git_info["tag_name"]):
            r=messagebox.askyesno("Versão disponível", "Nova versão está disponível para download.\n\nDeseja baixar a nova atualização?")
            if r==True:
                webbrowser.open('https://github.com/immlima/Tutorando', new=2)


window = Tk() 
window.title("Tutorando | Download de cartas de Magic")
window.iconphoto(TRUE, PhotoImage(file=os.path.join(os.path.abspath("."),os.path.join("Data","B.png"))))
window.resizable(FALSE,FALSE)

FramePrincipal = LabelFrame(window, text="Download de cartas de Magic: ")
FramePrincipal.grid(row=0, column=0, sticky=W, padx=5, pady=5)

def baixar_arquivo(url, endereço):
    reposta= requests.get(url)
    with open(endereço,'wb') as novo_arquivo:
        novo_arquivo.write(reposta.content)
namedeck=""

Frame_entry = LabelFrame(FramePrincipal, text="Preencha com uma carta ou selecione uma lista: ", padx=5, pady=5)

Entry1=Entry(Frame_entry, text="",bd=3, width=60)
Entry1.delete ( 0, last=999 )
Entry1.grid(row=0, column=1, sticky=NW, pady=2)

Frame_entry.grid(row=0, column=0,columnspan=3, sticky=NW, padx=5, pady=5)

def Procurando_lista():
    global End_file_deck
    global namedeck
    End_file_deck = filedialog.askopenfilename(title = "Selecione uma Lista", filetype = (("Lista de MTG", "*.txt"),("Todos os arquivos", "*.*")))
    namedeck=os.path.splitext(os.path.basename(open(End_file_deck).name))[0]
    Entry1.delete ( 0, last=999 )
    Entry1.insert (0, "Lista: "+namedeck )
    Entry1.grid(row=0, column=1, sticky=NW, pady=2)
Button(FramePrincipal, text = "Selecione uma Lista", command=Procurando_lista, width=15 ).grid(row=6, column=1, sticky=N, padx=5, pady=5)

var = StringVar()
cond = StringVar()
cond = "png"
Label(FramePrincipal, text ="   745 x 1040 png  ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
excard=PhotoImage(file =os.path.join(os.path.abspath("."),os.path.join("Data","png.png")) ).subsample(2, 2)
li=Label(FramePrincipal,image=excard)
li.excard = excard
li.grid(row=2, column=1, sticky=NW, padx=5, pady=5, rowspan=3)

def menu():
    global cond ,li
    cond = var.get()
    if cond=="small":
        li.grid_forget()
        Label(FramePrincipal, text ="   146 x 204 jpg   ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","png.png"))).subsample(2, 2)
    if cond=="normal":
        li.grid_forget()
        Label(FramePrincipal, text ="   488 x 680 jpg   ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","png.png"))).subsample(2, 2)
    if cond=="large": 
        li.grid_forget()
        Label(FramePrincipal, text ="   672 x 936 jpg   ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","png.png"))).subsample(2, 2)
    if cond=="png":
        li.grid_forget()
        Label(FramePrincipal, text ="   745 x 1040 png   ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","png.png"))).subsample(2, 2)
    if cond=="art_crop":
        li.grid_forget()
        Label(FramePrincipal, text ="          Arte          ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","art_crop.png"))).subsample(2, 2)
    if cond=="border_crop":
        li.grid_forget()
        Label(FramePrincipal, text ="   480 x 680 jpg   ", anchor="e").grid(row=5, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(os.path.abspath("."),os.path.join("Data","border_crop.png"))).subsample(2, 2)
    li=Label(FramePrincipal,image=excard)
    li.excard = excard
    li.grid(row=2, column=1, sticky=NW, padx=5, pady=5, rowspan=3)

labelframe1 = LabelFrame(FramePrincipal, text="Modelo: ")
labelframe1.grid(row=2, column=2, sticky=NW, pady=5)

Radiobutton(labelframe1, text="Pequeno", variable=var, value="small", command=menu ).grid(row=2, column=0, sticky=NW, padx=15)
Radiobutton(labelframe1, text="Médio", variable=var, value="normal", command=menu).grid(row=3, column=0, sticky=NW, padx=15)
Radiobutton(labelframe1, text="Grande", variable=var, value="large", command=menu).grid(row=4, column=0, sticky=NW, padx=15)
Radiobutton(labelframe1, text="Borda cortada", variable=var, value="border_crop", command=menu).grid(row=5, column=0, sticky=NW, padx=15)
Radiobutton(labelframe1, text="Arte destacada", variable=var, value="art_crop", command=menu).grid(row=6, column=0, sticky=NW, padx=15)
ss=Radiobutton(labelframe1, text="Png", variable=var, value="png", command=menu)
ss.select()
ss.grid(row=1, column=0, sticky=NW, padx=15)

flag_EN=True
var2 = StringVar()

def menu2():
    global flag_EN
    if var2.get()=="en":
        flag_EN=True
    else:
        flag_EN=False
labelframe2 = LabelFrame(FramePrincipal, text="Idioma: ")
labelframe2.grid(row=3, column=2, sticky=NW, pady=5)

Radiobutton(labelframe2, text="Português", variable=var2, value="pt", command=menu2).grid(row=1, column=0, sticky=NW, padx=15)
ss2=Radiobutton(labelframe2, text="English", variable=var2, value="en", command=menu2)
ss2.select()
ss2.grid(row=0, column=0, sticky=NW, padx=15)


times_anterrior=0
def single(card_deck,End_folder_img):
    global times_anterrior
    if card_deck[0:2]=="": 
        return 0
    if card_deck[0:1].isnumeric(): 
        card_deck = card_deck.split(" ", 1)
        card_deck[1]=card_deck[1].split('\n')
        card_deck[0]=card_deck[1][0]
    else:
        card_deck = card_deck.split("\n", 1)
    
    def sub_Basic_land(nome_da_carta):
        basicos = {
            "Planicie": "Plains",
            "Ilha": "Island",
            "Pantano": "Swamp",
            "Montanha": "Mountain",
            "Floresta": "Forest",
            "Ermo": "Wastes",
        }
        return basicos.get(nome_da_carta, nome_da_carta)
    url="https://api.scryfall.com/cards/named?fuzzy="+sub_Basic_land(card_deck[0].replace(":"," "))

    r = requests.get(url)

    if r.status_code == requests.codes.OK:
        if time.process_time_ns()-times_anterrior<100000000:
            time.sleep((time.process_time_ns()-times_anterrior)/1000000000)  #https://scryfall.com/docs/api  delay 100ms Rate Limits and Good Citizenship

        times_anterrior=time.process_time_ns()
        card_json=json.loads(r.text)
        global flag_EN

        if flag_EN==True:
            if card_json['lang']!="en":
                single(card_json['name'],End_folder_img)
                return 0
        else:
            if card_json['lang']=="en":
                url="https://api.scryfall.com/cards/"+card_json['set']+"/"+card_json['collector_number']+"/pt"
                r = requests.get(url)
                if r.status_code == requests.codes.OK:
                    if time.process_time_ns()-times_anterrior<100000000:
                        time.sleep((time.process_time_ns()-times_anterrior)/1000000000)  #https://scryfall.com/docs/api  delay 100ms Rate Limits and Good Citizenship

                    times_anterrior=time.process_time_ns()
                    if r.status_code == requests.codes.OK:
                        card_json=json.loads(r.text)

            if card_json['image_status'] != "highres_scan" and card_json['image_status'] != "lowres": 
                url="https://api.scryfall.com/cards/named?fuzzy="+card_json['name'].replace(":"," ")
                r = requests.get(url)
                if r.status_code == requests.codes.OK:
                    if time.process_time_ns()-times_anterrior<100000000:
                        time.sleep((time.process_time_ns()-times_anterrior)/1000000000)  #https://scryfall.com/docs/api  delay 100ms Rate Limits and Good Citizenship

                    times_anterrior=time.process_time_ns()
                    card_json=json.loads(r.text)
   
                
        if card_json['layout'] == "transform":
            img_card=card_json["card_faces"]
            img_card=img_card[0]
            img_card=img_card["image_uris"]
            img_card=img_card[cond]
            if cond == "png":
                name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].png"
            else:
                name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].jpg"                        
            name_card =os.path.join(End_folder_img,name_card)
            baixar_arquivo(img_card, name_card)
            img_card=card_json["card_faces"]
            img_card=img_card[1]
            img_card=img_card["image_uris"]
            img_card=img_card[cond]         
            if cond == "png":
                name_card=card_json['name'].replace("/"," ").replace(":"," ") +"-Transform ["+cond+"].png"
            else:
                name_card=card_json['name'].replace("/"," ").replace(":"," ") +"-Transform ["+cond+"].jpg"
            name_card =os.path.join(End_folder_img,name_card)
            baixar_arquivo(img_card, name_card)
        else:
            if card_json['layout'] == "modal_dfc":
                img_card=card_json["card_faces"]
                img_card=img_card[0]
                img_card=img_card["image_uris"]
                img_card=img_card[cond]
                if cond == "png":
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].png"
                else:
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].jpg"
                name_card =os.path.join(End_folder_img,name_card)
                baixar_arquivo(img_card, name_card)
                img_card=card_json["card_faces"]
                img_card=img_card[1]
                img_card=img_card["image_uris"]
                img_card=img_card[cond]
                if cond == "png":
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +"-Modal ["+cond+"].png"
                else:
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +"-Modal ["+cond+"].jpg"
                name_card =os.path.join(End_folder_img,name_card)
                baixar_arquivo(img_card, name_card)
            else:
                img_card=card_json["image_uris"]
                img_card=img_card[cond]
                if cond == "png":
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].png"
                else:
                    name_card=card_json['name'].replace("/"," ").replace(":"," ") +" ["+cond+"].jpg"
                name_card =os.path.join(End_folder_img,name_card)
                baixar_arquivo(img_card, name_card)
    else:
        messagebox.showinfo("Tutorando | Download de cartas de Magic", "Card não encontrado: "+card_deck[0])

def lista(End_folder_img):
    file_deck = open(End_file_deck, encoding='utf8')
    quantaslines=len(open(End_file_deck).readlines())
    counter=DoubleVar()
    counter.set(0)
    count=1
    top=Toplevel()
    top.resizable(FALSE,FALSE)
    top.geometry("250x145+700+400")
    pb=ttk.Progressbar(top,variable=counter,maximum=quantaslines )
    Button(top, text='Cancelar', command=top.destroy).place(x=160, y=110, width=65)
            
    for line_deck in file_deck:  
        tt=str(count)+"/"+str(quantaslines)
        counter.set(count)
        count += 1
        card_deck =line_deck
        if card_deck[0:1].isnumeric(): 
            card_deck = card_deck.split(" ", 1)
            card_deck[1]=card_deck[1].split('\n')
            card_deck[0]=card_deck[1][0]
        else:
            card_deck = card_deck.split("\n", 1)
        
        a=Label(top, text="                                                                                          " ,bd=3)
        a.place(x=10, y=25)
        a=Label(top, text=card_deck[0] ,bd=3)
        a.place(x=10, y=25)
        b=Label(top, text="                                                                                          " ,bd=3)
        b.place(x=10, y=50)
        b=Label(top, text=tt ,bd=3)
        b.place(x=10, y=50)
        pb.place(x=50, y=80, width=150)
        top.update()
        top.deiconify()
        single(card_deck[0],End_folder_img)
    global namedeck
    top.destroy()
    messagebox.showinfo("Tutorando | Download de cartas de Magic", "Concluído o Download: "+namedeck)

def save_img_card():
    if Entry1.get() != '':
        End_folder_img = filedialog.askdirectory(title = "Escolha um diretório para salvar os cards")
        if End_folder_img!='' :
            if Entry1.get()[0:7]=='Lista: ':
                lista(End_folder_img)
            else:
                top=Toplevel()
                top.resizable(FALSE,FALSE)
                top.geometry("250x145+700+400")
                top.deiconify()
                min=DoubleVar()
                min.set(1)
                max=2
                pb=ttk.Progressbar(top,variable=min,maximum=max )
                Button(top, text='Cancelar', command=top.destroy).place(x=160, y=110, width=65)
                a=Label(top, text=Entry1.get() ,bd=3)
                a.place(x=10, y=25)
                b=Label(top, text="1/1" ,bd=3)
                b.place(x=10, y=50)
                pb.place(x=50, y=80, width=150)
                top.update()
                single(Entry1.get(),End_folder_img)
                min.set(2)
                top.update()
                top.destroy()
    else:
        messagebox.showinfo("Tutorando | Download de cartas de Magic", "Preencha com uma card ou selecione uma lista")

def buttonFramePrincipal(event=None):
    if Entry1.get() != "" :
        save_img_card()
    else:
        Procurando_lista()  

def exemplo():
    top=Toplevel()
    top.resizable(FALSE,FALSE)
    top.geometry("345x195+700+400")
    top.deiconify()
    Label(top, text ="Você pode usar qualquer um dos seguintes \n formatos em listas:").grid(row=0, column=0, columnspan=2, sticky=N, padx=20, pady=10)
    lff1=LabelFrame(top, text ="Formato 1")
    lff1.grid(row=1, column=0, sticky=N, padx=15)
    Label(lff1, text ="4 Ancient Den").grid(row=2, column=0, sticky=W, padx=15)
    Label(lff1, text ="2 Arcbound Ravager").grid(row=3, column=0, sticky=W, padx=15)
    Label(lff1, text ="4 Welding Jar").grid(row=4, column=0, sticky=W, padx=15)
    Label(lff1, text ="4 Ornithopter").grid(row=5, column=0, sticky=W, padx=15)
    Label(lff1, text ="etc... ").grid(row=6, column=0, sticky=W, padx=15)
    lff2=LabelFrame(top, text ="Formato 2")
    lff2.grid(row=1, column=1, sticky=N, padx=15)
    Label(lff2, text ="Ancient Den").grid(row=2, column=1, sticky=W, padx=15)
    Label(lff2, text ="Arcbound Ravager").grid(row=3, column=1, sticky=W, padx=15)
    Label(lff2, text ="Welding Jar").grid(row=4, column=1, sticky=W, padx=15)
    Label(lff2, text ="Ornithopter").grid(row=5, column=1, sticky=W, padx=15)
    Label(lff2, text ="etc... ").grid(row=6, column=1, sticky=W, padx=15)
    top.update()
  
b1=Button(Frame_entry, text = "🔻", anchor="e" , command=buttonFramePrincipal)
b1.grid(row=0, column=3, padx=5)                   
Button(Frame_entry, text = " ? ", anchor="e" , command=exemplo).grid(row=0, column=4, padx=5)                   
Button(FramePrincipal, text = "Baixar Cartas", command=save_img_card, width=10).grid(row=6, column=2, sticky=NW, padx=5, pady=5)
versao()
window.bind('<Return>',buttonFramePrincipal)
window.mainloop()