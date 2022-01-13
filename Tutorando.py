import os
import time
import json
import requests
import webbrowser
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import filedialog, messagebox, ttk 

#|---Verificaçao da versao---|
version="1.1.0"
def versao():
    url="https://api.github.com/repos/immlima/Tutorando/releases/latest"
    v = requests.get(url, timeout=None)

    if v.status_code == requests.codes.OK:
        git_info=json.loads(v.text)
        if version!=str(git_info["tag_name"]):
            if messagebox.askyesno("Versão disponível", "Nova versão está disponível para download.\n\nDeseja baixar a nova atualização?\n\n"+git_info["body"])==True:
                webbrowser.open('https://github.com/immlima/Tutorando', new=2)   
#|----------------------------|
caminho = os.path.abspath(".")

tema="breeze"
window =  ThemedTk(theme=tema)
window.set_theme(tema)

window.title("Tutorando | Download de cartas de Magic")
window.iconphoto(TRUE, PhotoImage(file=os.path.join(caminho,"Data","B.png")))
window.resizable(FALSE,FALSE)

FramePrincipal = ttk.LabelFrame(window, text=" Download de cartas de Magic: ")
FramePrincipal.grid(row=0, column=0, sticky=W, padx=5, pady=5)

Frame_entry = ttk.LabelFrame(FramePrincipal, text=" Preencha com uma carta desejada ou selecione uma lista: ")

Entry1= ttk.Entry(Frame_entry, text="", width=50)
Entry1.delete ( 0, last=999 )
Entry1.grid(row=0, column=0,columnspan=3, sticky=E, padx=5, pady=1)

def exemplo():
    top=Toplevel()
    top.resizable(FALSE,FALSE)
    top.geometry("355x195+700+400")
    top.deiconify()
    ttk.Label(top, text ="Você pode usar qualquer um dos seguintes \n formatos em listas:").grid(row=0, column=0, columnspan=2, sticky=N, padx=20, pady=10)
    lff1=ttk.LabelFrame(top, text =" Formato 1")
    lff1.grid(row=1, column=0, sticky=N, padx=15)
    ttk.Label(lff1, text ="4 Ancient Den").grid(row=2, column=0, sticky=W, padx=15)
    ttk.Label(lff1, text ="2 Arcbound Ravager").grid(row=3, column=0, sticky=W, padx=15)
    ttk.Label(lff1, text ="4 Welding Jar").grid(row=4, column=0, sticky=W, padx=15)
    ttk.Label(lff1, text ="4 Ornithopter").grid(row=5, column=0, sticky=W, padx=15)
    ttk.Label(lff1, text ="etc... ").grid(row=6, column=0, sticky=W, padx=15)
    lff2=ttk.LabelFrame(top, text =" Formato 2")
    lff2.grid(row=1, column=1, sticky=N, padx=15)
    ttk.Label(lff2, text ="Ancient Den").grid(row=2, column=1, sticky=W, padx=15)
    ttk.Label(lff2, text ="Arcbound Ravager").grid(row=3, column=1, sticky=W, padx=15)
    ttk.Label(lff2, text ="Welding Jar").grid(row=4, column=1, sticky=W, padx=15)
    ttk.Label(lff2, text ="Ornithopter").grid(row=5, column=1, sticky=W, padx=15)
    ttk.Label(lff2, text ="etc... ").grid(row=6, column=1, sticky=W, padx=15)
    top.update()

ttk.Button(Frame_entry, text = "?", command=exemplo, width=2).grid(row=0, column=4, padx=5) 
Frame_entry.grid(row=0, column=0,columnspan=3, sticky=N, padx=5, pady=5)

ttk.Label(Frame_entry, text ="   OU  ", anchor="e").grid(row=1, column=0,columnspan=9999, sticky=N, pady=5)

namedeck=""
def Procurando_lista():
    global End_file_deck
    global namedeck
    End_file_deck = filedialog.askopenfilename(title = "Selecione uma Lista", filetype = (("Lista de MTG", "*.txt"),("Todos os arquivos", "*.*")))
    namedeck=os.path.splitext(os.path.basename(open(End_file_deck).name))[0]
    Entry1.delete ( 0, last=999 )
    Entry1.insert (0, "Lista: "+namedeck )
    Entry1.grid(row=0, column=1, sticky=NW, pady=2)
ttk.Button(Frame_entry, text = "Selecione uma Lista", command=Procurando_lista, width=55 ).grid(row=2, column=0,columnspan=6, sticky=N, padx=5, pady=5)

ttk.Label(FramePrincipal, text ="   745 x 1040 png  ").grid(row=98, column=1, sticky=N, padx=5, pady=5)
excard=PhotoImage(file =os.path.join(caminho,os.path.join("Data","png.png")) ).subsample(2, 2)
li=ttk.Label(FramePrincipal,image=excard)
li.excard = excard
li.grid(row=2, column=1, sticky=NW, padx=5, pady=5, rowspan=90)

var = StringVar()
cond = StringVar()
def menu_modelo():
    global cond ,li
    cond = var.get()
    if cond=="small":
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="   146 x 204 jpg   ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","png.png")).subsample(2, 2)
    if cond=="normal":
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="   488 x 680 jpg   ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","png.png")).subsample(2, 2)
    if cond=="large": 
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="   672 x 936 jpg   ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","png.png")).subsample(2, 2)
    if cond=="png":
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="   745 x 1040 png   ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","png.png")).subsample(2, 2)
    if cond=="art_crop":
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="          Arte          ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","art_crop.png")).subsample(2, 2)
    if cond=="border_crop":
        li.grid_forget()
        ttk.Label(FramePrincipal, text ="   480 x 680 jpg   ", anchor="e").grid(row=98, column=1, sticky=N, padx=5, pady=5)
        excard=PhotoImage(file = os.path.join(caminho,"Data","border_crop.png")).subsample(2, 2)
    li=ttk.Label(FramePrincipal,image=excard)
    li.excard = excard
    li.grid(row=2, column=1, sticky=NW, padx=5, pady=5, rowspan=90)

labelframe1 = ttk.LabelFrame(FramePrincipal, text=" Modelo: ", width=100)
labelframe1.grid(row=2, column=0, sticky=NW, pady=5, padx=5)

ss=ttk.Radiobutton(labelframe1, text="Png", variable=var, value="png", command=menu_modelo)
ttk.Radiobutton(labelframe1, text="Pequeno", variable=var, value="small", command=menu_modelo ).grid(row=2, column=0, sticky=NW, padx=15)
ttk.Radiobutton(labelframe1, text="Médio", variable=var, value="normal", command=menu_modelo).grid(row=3, column=0, sticky=NW, padx=15)
ttk.Radiobutton(labelframe1, text="Grande", variable=var, value="large", command=menu_modelo).grid(row=4, column=0, sticky=NW, padx=15)
ttk.Radiobutton(labelframe1, text="Borda cortada", variable=var, value="border_crop", command=menu_modelo).grid(row=5, column=0, sticky=NW, padx=15)
ttk.Radiobutton(labelframe1, text="Arte destacada", variable=var, value="art_crop", command=menu_modelo).grid(row=6, column=0, sticky=NW, padx=15)
ss.grid(row=1, column=0, sticky=NW, padx=15)
ss.invoke()

flag_EN=True
var2 = StringVar()
def menu_idioma():
    global flag_EN
    if var2.get()=="en":
        flag_EN=True
    else:
        flag_EN=False

labelframe2 = ttk.LabelFrame(FramePrincipal, text=" Idioma: ", width=100)
labelframe2.grid(row=3, column=0, sticky=NW, padx=5)

ttk.Radiobutton(labelframe2, text="Português       ", variable=var2, value="pt", command=menu_idioma).grid(row=1, column=0, sticky=NW, padx=15)
ss2=ttk.Radiobutton(labelframe2, text="English", variable=var2, value="en", command=menu_idioma)
ss2.grid(row=0, column=0, sticky=NW, padx=15)
ss2.invoke()

def baixar_arquivo(url, endereço):
    reposta= requests.get(url, timeout=None)
    if reposta.status_code == requests.codes.OK:
        with open(endereço,'wb') as novo_arquivo:
            novo_arquivo.write(reposta.content)

times_times_anterior=time.time_ns()
def single(card_deck,End_folder_img):
    global times_times_anterior
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
    
    def rq(url):
        global times_times_anterior

        r = requests.get(url, timeout=None)
        if time.time_ns()-times_times_anterior<100000000:
            time.sleep((time.time_ns()-times_times_anterior)/1000000000)  #https://scryfall.com/docs/api  delay 100ms Rate Limits and Good Citizenship
        times_times_anterior=time.time_ns()
        #print(r.status_code)
        return r
    r=rq(url)
    card_json=json.loads(r.text)    
    global flag_EN
    if flag_EN==True: #tag em English
        if card_json['image_status'] != "highres_scan":
            url =f"https://api.scryfall.com/cards/search?order=released&q=oracleid%3A{ card_json['oracle_id'] }&unique=prints"
            r=rq(url)
            if r.status_code == requests.codes.OK:
                info_card_prints=json.loads(r.text)
                for card_json in info_card_prints['data']:
                    if card_json['image_status'] == "highres_scan":
                        break
                else:
                    url="https://api.scryfall.com/cards/named?fuzzy="+sub_Basic_land(card_deck[0].replace(":"," "))
                    r=rq(url)
                    card_json=json.loads(r.text)  
        
        if card_json['lang']!="en": # PT -> EN
            single(card_json['name'],End_folder_img)
            return 0
    else: #tag em Portugues
        if card_json['object']=="card":
            if card_json['lang']=="en": # EN -> PT

                url="https://api.scryfall.com/cards/"+card_json['set']+"/"+card_json['collector_number']+"/pt"
                r=rq(url)
                if r.status_code != requests.codes.OK:
                    #print("procurando versao pt")
                    url =f"https://api.scryfall.com/cards/search?order=released&q=oracleid%3A{ card_json['oracle_id'] }&unique=prints"
                    r=rq(url)
                    if r.status_code == requests.codes.OK:
                        info_card_prints=json.loads(r.text)
                        for cards_english in info_card_prints['data']:
                            
                            url="https://api.scryfall.com/cards/"+cards_english['set']+"/"+cards_english['collector_number']+"/pt"
                            r=rq(url)

                            if r.status_code == requests.codes.OK:
                                break
                        else:
                            #print(card_json)
                            url="https://api.scryfall.com/cards/named?fuzzy="+sub_Basic_land(card_json["name"].replace(":"," "))
                            r=rq(url)
                card_json=json.loads(r.text)
                
        if card_json['object']=="card": #NOT highres_scan and NOT lowres
            if card_json['image_status'] != "highres_scan" and card_json['image_status'] != "lowres": 
                url="https://api.scryfall.com/cards/named?fuzzy="+card_json['name'].replace(":"," ")
                r=rq(url)
                card_json=json.loads(r.text)


    if "printed_name" in card_json:
        printed_name=card_json['printed_name'].replace(":"," ").replace("/"," ")
    else:
        printed_name=card_json['name'].replace(":"," ").replace("/"," ")

    if card_json['layout'] == "transform":
        img_card=card_json["card_faces"]
        img_card=img_card[0]
        img_card=img_card["image_uris"]
        img_card=img_card[cond]
        print(cond)
        if cond == "png":
            name_card=f"{printed_name} [{card_json['lang']}] [{cond}].png"            
        else:
            name_card=printed_name + " [" + card_json['lang'] + "]" + " [" + cond + "].jpg"                        
        name_card =os.path.join(End_folder_img,name_card)
        baixar_arquivo(img_card, name_card)

        img_card=card_json["card_faces"]
        img_card=img_card[1]
        img_card=img_card["image_uris"]
        img_card=img_card[cond]         
        if cond == "png":
            name_card=printed_name+"-Transform [" + card_json['lang'] + "]" + " [" + cond + "].png"
        else:
            name_card=printed_name+"-Transform [" + card_json['lang'] + "]" + " [" + cond + "].jpg"
        name_card =os.path.join(End_folder_img,name_card)
        baixar_arquivo(img_card, name_card)
    else:
        if card_json['layout'] == "modal_dfc":
            img_card=card_json["card_faces"]
            img_card=img_card[0]
            img_card=img_card["image_uris"]
            img_card=img_card[cond]
            if cond == "png":
                name_card=printed_name + " [" + card_json['lang'] + "]" + " [" + cond + "].png"
            else:
                name_card=printed_name + " [" + card_json['lang'] + "]" + " [" + cond + "].jpg"
            name_card =os.path.join(End_folder_img,name_card)
            baixar_arquivo(img_card, name_card)

            img_card=card_json["card_faces"]
            img_card=img_card[1]
            img_card=img_card["image_uris"]
            img_card=img_card[cond]
            if cond == "png":
                name_card=printed_name+"-Modal [" + card_json['lang'] + "]" + " [" + cond + "].png"
            else:
                name_card=printed_name+"-Modal [" + card_json['lang'] + "]" + " [" + cond + "].jpg"
            name_card =os.path.join(End_folder_img,name_card)
            baixar_arquivo(img_card, name_card)
            
        else:
            img_card=card_json["image_uris"]
            img_card=img_card[cond]
            if cond == "png":
                name_card=printed_name + " [" + card_json['lang'] + "]" + " [" + cond + "].png"
            else:
                name_card=printed_name + " [" + card_json['lang'] + "]" + " [" + cond + "].jpg"
            name_card =os.path.join(End_folder_img,name_card)
            baixar_arquivo(img_card, name_card)

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
    ttk.Button(top, text='Cancelar', command=top.destroy).place(x=140, y=110)
            
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
        
        a=ttk.Label(top, text="                                                                                          " )
        a.place(x=10, y=25)
        a=ttk.Label(top, text=card_deck[0] )
        a.place(x=10, y=25)
        b=ttk.Label(top, text="                                                                                          " )
        b.place(x=10, y=50)
        b=ttk.Label(top, text=tt )
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
                #print(End_folder_img)
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
                ttk.Button(top, text='Cancelar', command=top.destroy).place(x=160, y=110, width=65)
                a=ttk.Label(top, text=Entry1.get() )
                a.place(x=10, y=25)
                b=ttk.Label(top, text="1/1" )
                b.place(x=10, y=50)
                pb.place(x=50, y=80, width=150)
                top.update()
                single(Entry1.get(),End_folder_img)
                min.set(2)
                top.update()
                top.destroy()
    else:
        messagebox.showinfo("Tutorando | Download de cartas de Magic", "Preencha com uma carta desejada ou selecione uma lista")

ttk.Button(FramePrincipal, text = "Baixar Cartas", command=save_img_card, width=55).grid(row=99, column=0, columnspan=6, sticky=N, padx=5, pady=5)

def buttonFramePrincipal(event=None):
    if Entry1.get() != "" :
        save_img_card()
    else:
        Procurando_lista()  
window.bind('<Return>',buttonFramePrincipal)
versao()
window.mainloop()