import tkinter
from tkinter import messagebox
from psw_gen import PasswordGenerator
import json

# -------------------------- PASSWORD GENERATOR ------------------------------- #
psw_gen = PasswordGenerator()


def generate_password():
    psw_name.delete(0, 'end')
    password = psw_gen.generate()
    psw_name.insert(0, password)


# --------------------------   Search password    ----------------------------- #
def search():
    webname = web_name.get()
    emailname = email_name.get()
    with open("entry.json", "r") as f:
        r_data = json.load(f)
    for x in r_data[webname]:
        if x['email'] == emailname:
            print(x['email'])
            print(x['password'])
            psw_name.insert(0,x['password'])



# -------------------------- Reset Entry Field  ------------------------------- #
def reset():
    web_name.delete(0, 'end')
    email_name.delete(0, 'end')
    psw_name.delete(0, 'end')
    web_name.focus()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webname = web_name.get()
    emailname = email_name.get()
    pswname = psw_name.get()
    web_name.focus()
    new_data = {
        webname: [
                {'email': emailname, 'password': pswname}
            ]
    }

    if len(webname) == 0 or len(emailname) == 0 or len(pswname) == 0:
        messagebox.showerror(title="Error", message="please fill all field...")
    else:
        is_ok = messagebox.askokcancel(title="password_manager",
                                       message=f"please check your credential ?\nWebsite : {webname}\nEmail :{emailname}\nPassword :{pswname}\n ")
        if is_ok:
            try:
                with open("entry.json", "r") as f:
                    data = json.load(f)
                print(data)
                if webname in data:
                    print("yes")
                    for x in data[webname]:
                        if x['email'] != emailname:
                            print("no email found")
                            data["amazon"].append({'email': emailname, 'password': pswname})
                            print(data)
                        else:
                            print("fuck")
                            print("no email found")
                            change = messagebox.askokcancel(title="some credential found", message=f"{emailname}\nAre you updating Password ?")
                            if change:
                                x['password'] = pswname
                            break
                else:
                    data.update(new_data)
            except Exception:
                with open("entry.json", 'w') as f:
                    json.dump(new_data, f, indent=4)
                    print("except added")
            else:
                with open("entry.json", 'w') as f:
                    json.dump(data, f, indent=4)
                    print("else added")
            finally:
                web_name.delete(0, 'end')
                email_name.delete(0, 'end')
                psw_name.delete(0, 'end')
                web_name.focus()


# ---------------------------- UI SETUP ------------------------------- #
w = tkinter.Tk()
w.title("Password-Manager")
w.minsize(width=500, height=500)
w.config(bg="white")

website = tkinter.StringVar()
email = tkinter.StringVar()
password = tkinter.StringVar()

logo_img = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg="white")
canvas.create_image(100, 100, image=logo_img)
canvas.place(x=170, y=50)

web_lbl = tkinter.Label(text="Website                :", bg="white")
web_lbl.place(x=100, y=300)

web_name = tkinter.Entry(width=40)
web_name.place(x=220, y=300)
web_name.focus()

email_lbl = tkinter.Label(text="Email/Username :", bg="white")
email_lbl.place(x=100, y=350)

email_name = tkinter.Entry(width=40)
email_name.place(x=220, y=350)
email_name.insert(0, "apser.siraj@gmail.com")

psw_lbl = tkinter.Label(text="Password             :", bg="white")
psw_lbl.place(x=100, y=400)

psw_name = tkinter.Entry(w, width=20)
psw_name.place(x=220, y=400)

gen_psw_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_psw_btn.place(x=350, y=400)

reset_btn = tkinter.Button(text="Reset", command=reset)
reset_btn.place(x=150, y=440)

add_btn = tkinter.Button(text="ADD", command=save)
add_btn.place(x=250, y=440)

search_btn = tkinter.Button(text="Search", command=search)
search_btn.place(x=350, y=440)

w.mainloop()
