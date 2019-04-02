import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#メール送る関数
def send_mail():
    import smtplib
    from email.mime.text import MIMEText
    message = "テスト"
    msg = MIMEText(message)
    msg["Subject"] = "サブジェクト"
    msg["To"] = eto.get()
    msg["From"] = efrom.get()
    server = smtplib.SMTP(server_info.get(), port_info.get())
    server.send_message(msg)
    server.quit()

#参照ボタンの処理
def attach_click():
    fTyp = [("","*.eml")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    emlfile1.set(filepath)    
    
#UIの設定
root = Tk()
root.title('メール送るやつ')
main_frame = ttk.Frame(root)
server_label = ttk.Label(main_frame, text='サーバ情報')
port_label = ttk.Label(main_frame, text='port')

#各種の入力値の指定
eto = StringVar()
efrom = StringVar()
server_info = StringVar()
port_info = IntVar()
emlfile1 = StringVar()

#envelop Toのテキストボックス
eto_label = ttk.Label(main_frame, text='宛先')
eto_entry = ttk.Entry(main_frame, textvariable=eto) 

#envelop fromのテキストボックス
efrom_label = ttk.Label(main_frame, text='送信者')
efrom_entry = ttk.Entry(main_frame, textvariable=efrom)

#サーバ情報とポート番号
server_entry = ttk.Entry(main_frame, textvariable=server_info) 
port_entry = ttk.Entry(main_frame, textvariable=port_info)

#参照ファイルパス表示テキストボックス
emlfile1_label = ttk.Label(main_frame, text='eml pass:')
emlfile1_entry = ttk.Entry(main_frame, textvariable=emlfile1)

# 参照ボタンの作成
attach_btn = ttk.Button(main_frame, text=u'参照', command=attach_click)

#送信ボタン
send_button = ttk.Button(main_frame, text='送信！', command=send_mail)


#UIの位置
main_frame.grid(row=0,column=0,sticky=(N,E,S,W))

server_label.grid(row=1,column=1,sticky=W)
server_entry.grid(row=1,column=2,sticky=W)
port_label.grid(row=1,column=3,ipadx=5,sticky=W)
port_entry.grid(row=1,column=4,ipadx=5,sticky=W)

efrom_label.grid(row=2,column=1,sticky=W)
efrom_entry.grid(row=2,column=2,sticky=W)

eto_label.grid(row=3,column=1,sticky=W)
eto_entry.grid(row=3,column=2,sticky=W)

emlfile1_label.grid(row=4,column=1,sticky=W)
emlfile1_entry.grid(row=4,column=2,sticky=W)
attach_btn.grid(row=4,column=3,sticky=W)

send_button.grid(row=5,column=2,sticky=W)


#起動
for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()