from Tkinter import*
from tkMessageBox import*
root=Tk()
root.geometry=(800*800)
Label(root,text="NAME: AYUSH JAIN",font="Aerial 15 bold").grid(row=0,column=0,columnspan=4)
Label(root,text="Enroll Number: 151265",font="Aerial 15 bold").grid(row=1,column=0,columnspan=4)
Label(root,text="BATCH: B2",font="Aerial 15 bold").grid(row=2,column=0,columnspan=4)
Label(root,text="EMAIL ID: ayushjain7398@gmail.com",font="Aerial 15 bold").grid(row=3,column=0,columnspan=4)
Label(root,text="BRANCH: C.S.E",font="Aerial 15 bold").grid(row=4,column=0,columnspan=4)
Label(root,text="PROJECT NAME: Insurance Policy Detail System: ",font="Aerial 15 bold").grid(row=6,column=0,columnspan=4)
Label(root,text="CONTACT INFO.: 8871683035",font="Aerial 15 bold").grid(row=5,column=0,columnspan=4)
Label(root,text="    ",font="Aerial 15 bold").grid(row=7,column=0,columnspan=4)
Label(root,text="    ",font="Aerial 15 bold").grid(row=8,column=0,columnspan=4)
Label(root,text="press OK to start project",font="Aerial 15 bold",fg='blue').grid(row=9,column=0)
Button(root,text='OK',width=30,height=3,command=lambda:ok(),bd=3,fg='red',bg='black').grid(row=10,column=1)
def ok():
    import  sqlite3
    con=sqlite3.Connection("ys")
    cur=con.cursor()
    cur.execute("create table policyx(code number primary key, pname varchar2(50),featcher varchar2(100),time varchar2(15),money_d_peryear varchar2(40),profit varchar2(30))")
    a=()

    cur.execute("insert into policyx values(151265,'pname=jivan bima','feacher=this is short time policy','time=2years','money_d_peryear=Rs.1200','profit=1000')",a)
    cur.execute("insert into policyx values(151266,'pname=jeevan amrit','feacher=this can full-fill about your needs','time=5years','money_d_peryear=Rs.1500','profit=2000')",a)
    cur.execute("insert into policyx values(151267,'pname=jivan jeevan saral','feacher=by taking this policy you well tension free about future','time=7years','money_d_peryear: Rs.1000','profit=8500')",a)
    cur.execute("insert into policyx values(151268,'pname=:profit plus policy','feacher=In this after complition of policy you get good profit','time=3years','money_d_peryear=Rs.1300','profit=9000')",a)
    cur.execute("insert into policyx values(151269,'pname=komal jeevan','feacher=then is lyf time policy','time=9years','money_d_peryear=Rs.2400','profit=7700')",a)
    cur.execute("insert into policyx values(151270,'pname=jeevan suraksha','feacher=this is for your security','time=11years','money_d_peryear=rs.3300','profit=8800')",a)
    cur.execute("insert into policyx values(151271,'pname=bima gold','feacher=Best policy to invest and get profit in less time','time=9years','money_d_peryear=rs.1500','profit=9600')",a)
    cur.execute("insert into policyx values(151272,'pname=shiksha policy','feacher=this policy is for future education of your child ','time=4years','money_d_peryear=rs.1600','profit=5500')",a)
    cur.execute("insert into policyx values(151273,'pname=jeevan vishvash','feacher=this policy will return you good profit but req. is your trust','time=8years','money_d_peryear=rs.1700','profit=6000')",a)
    cur.execute("insert into policyx values(151274,'pname=jeevan tarang','feacher=this is our policy which give you profit always after completion','time=6years','money_d_peryear=rs.1900','profit=7000')",a)
    cur.execute("insert into policyx values(151275,'pname=jeevan aanand','feacher=this is a plane to give u a healthy life','time=12years','money_d_peryear=rs.3300','profit=9000')",a)
    cur.execute("insert into policyx values(151276,'pname=jeevan rakshak','feacher=policy for your sicurity','time=13years','money_d_peryear=rs.3700','profit=10000')",a)
    cur.execute("insert into policyx values(151277,'pname=easy life','feacher=after completing this u get good future without tnsion of savings','time=14years','money_d_peryear=rs.2700','profit=14000')",a)
    cur.execute("insert into policyx values(151278,'pname=education plus','feacher=for the future dreams for your child ','time=15years','money_d_peryear=rs.2900','profit=3000')",a)
    cur.execute("insert into policyx values(151279,'pname=jeevan aadhar','feacher=to get an achievement we help you after taking this policy','time=16years','money_d_peryear=rs.3000','profit=10000')",a)

    root=Tk()
    x=IntVar()
    root.title("Insurance policy detail system")
    Label(root,text="Insurance Policy Detail System:",font="Aerial 20 bold",bg='green').grid(row=0,column=0,columnspan=4,sticky='W')

    Label(root,text="Types Of All Policy:",font="Aerial 15 bold",bg='yellow').grid(row=1,column=0,columnspan=4)
    Label(root,text="151265:jeevan bima",font="Aerial",bg='dark gray').grid(row=2,column=0,sticky=E+W+N+S)
    Label(root,text="151266:jeevan amrit",font="Aerial",bg='dark gray').grid(row=2,column=1,sticky=E+W+N+S)
    Label(root,text="151267:jeevan saral",font="Aerial",bg='dark gray').grid(row=2,column=2,sticky=E+W+N+S)
    Label(root,text="151268:profit plus policy",font="Aerial",bg='dark gray').grid(row=2,column=3,sticky=E+W+N+S)

    Label(root,text="151269:komal jeevan",font="Aerial",bg='dark gray').grid(row=2,column=4,sticky=E+W+N+S)
    Label(root,text="151270:jeevan suraksha",font="Aerial",bg='dark gray').grid(row=3,column=0,sticky=E+W+N+S)
    Label(root,text="151271:bima gold",font="Aerial",bg='dark gray').grid(row=3,column=1,sticky=E+W+N+S)
    Label(root,text="151272:shiksha policy",font="Aerial",bg='dark gray').grid(row=3,column=2,sticky=E+W+N+S)
    Label(root,text="151273:jeevan vishvash",font="Aerial",bg='dark gray').grid(row=3,column=3,sticky=E+W+N+S)

    Label(root,text="151274:jeevan tarang",font="Aerial",bg='dark gray').grid(row=3,column=4,sticky=E+W+N+S)
    Label(root,text="151275:jeevan aanand",font="Aerial",bg='dark gray').grid(row=4,column=0,sticky=E+W+N+S)
    Label(root,text="151276:jeevan rakshak",font="Aerial",bg='dark gray').grid(row=4,column=1,sticky=E+W+N+S)
    Label(root,text="151277:easy life",font="Aerial",bg='dark gray').grid(row=4,column=2,sticky=E+W+N+S)
    Label(root,text="151278:education plus",font="Aerial",bg='dark gray').grid(row=4,column=3,sticky=E+W+N+S)

    Label(root,text="151279:jeevan aadhar",font="Aerial",bg='dark gray').grid(row=4,column=4,sticky=E+W+N+S)
    Label(root,text=".....",font="Aerial",bg='dark gray').grid(row=5,column=0,sticky=E+W+N+S)
    Label(root,text=".....",font="Aerial",bg='dark gray').grid(row=5,column=1,sticky=E+W+N+S)
    Label(root,text="......",font="Aerial",bg='dark gray').grid(row=5,column=2,sticky=E+W+N+S)
    Label(root,text="......",font="Aerial",bg='dark gray').grid(row=5,column=3,sticky=E+W+N+S)
    Label(root,text="......",font="Aerial",bg='dark gray').grid(row=5,column=4,sticky=E+W+N+S)
    Label(root,text="_____________________________________________________________________________________________________________________________________________________________________________",bg='black').grid(row=7,column=0,columnspan=5)

    Label(root,text="ENTER POLICY CODE FOR DETAILS:",font="Aerial 15 bold",bg='gray').grid(row=9,column=0,columnspan=4,sticky='W')
    e=Entry(root,width=12,font='Arial 32',bd=3,justify='left')
    e.grid(row=11,column=0,columnspan=4)
    def add_entry(x):
        e.insert(16,x)
    def clearall():
        e.delete(0,END)
    def clear():
        e.delete(len(e.get())-1)
    def show():
        q=int(e.get())
        cur.execute("select * from policyx where code=(?)",(q,))
        a=cur.fetchall()
        showinfo('details',a)
        print a
    def showall():
        cur.execute("select * from policyx")
        a=cur.fetchall()
        showinfo('All details',a)
        print a
    Label(root,text="  ").grid(row=8,column=0)
    Label(root,text="  ").grid(row=10,column=0)
    Label(root,text="  ").grid(row=12,column=0)
    Label(root,text="  ").grid(row=14,column=0)
    Button(root,text='7',width=5,height=3,command=lambda:add_entry('7'),bg='black',bd=5,foreground='light blue').grid(row=15,column=1)
    Button(root,text='8',width=5,height=3,command=lambda:add_entry('8'),bg='black',bd=5,foreground='light blue').grid(row=15,column=1,columnspan=2)
    Button(root,text='9',width=5,height=3,command=lambda:add_entry('9'),bg='black',bd=5,foreground='light blue').grid(row=15,column=1,columnspan=3)
    Button(root,text='4',width=5,height=3,command=lambda:add_entry('4'),bg='black',bd=5,foreground='light blue').grid(row=16,column=1)
    Button(root,text='5',width=5,height=3,command=lambda:add_entry('5'),bg='black',bd=5,foreground='light blue').grid(row=16,column=1,columnspan=2)
    Button(root,text='6',width=5,height=3,command=lambda:add_entry('6'),bg='black',bd=5,foreground='light blue').grid(row=16,column=1,columnspan=3)
    Button(root,text='1',width=5,height=3,command=lambda:add_entry('1'),bg='black',bd=5,foreground='light blue').grid(row=17,column=1)
    Button(root,text='2',width=5,height=3,command=lambda:add_entry('2'),bg='black',bd=5,foreground='light blue').grid(row=17,column=1,columnspan=2)
    Button(root,text='3',width=5,height=3,command=lambda:add_entry('3'),bg='black',bd=5,foreground='light blue').grid(row=17,column=1,columnspan=3)
    Button(root,text='0',width=5,height=3,command=lambda:add_entry('0'),bg='black',bd=5,foreground='light blue').grid(row=15,column=2,columnspan=4)
    Button(root,text='C',width=5,height=3,command=lambda:clearall(),bd=5,bg='black',foreground='light blue').grid(row=16,column=2,columnspan=4)
    Button(root,text='CE',width=5,height=3,command=lambda:clear(),bd=5,bg='black',foreground='light blue').grid(row=17,column=2,columnspan=4)
    Button(root,text="Show",bg='orange',command=show).grid(row=13,column=1)
    Button(root,text="Showall",bg='orange',command=showall).grid(row=13,column=2)
    root.mainloop()

root.mainloop()   
