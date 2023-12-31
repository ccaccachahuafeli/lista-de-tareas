from tkinter import *
from tkinter import ttk
from config import *
from Funciones import *

class InterfazApp(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_widget()

    #metodo propio vamos a darle las configuraciones basicas para mostrar nuestra ventana
    def configurar_ventana(self):
        self.title(f"{TITULO_APP} {HORA_ACTUAL}")
        self.configure(bg=COLOR_FONDO_PRIMARIO)
        self.resizable(0,0)
        self.attributes("-alpha",0.96)
        w,h=870,400
        centrar_ventana(self,w,h)

    def construir_widget(self):

        #CAJITA DE TEXTOS
        self.cajas_textos=LabelFrame(self,text="Cajas de texto",width=150,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_textos.grid(row=0,column=0,pady=20,padx=20)
        #caja para capturar el nombre
        self.label_nombre=Label(self.cajas_textos,text="Nombres",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.nombre_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.nombre_texto.pack()

        #caja para capturar el actividades
        self.label_actividades=Label(self.cajas_textos,text="Actividades",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.actividades_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.actividades_texto.pack()
        #caja para capturar el horarios
        self.label_horarios=Label(self.cajas_textos,text="Horarios",bg=COLOR_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
        self.horarios_texto=Entry(self.cajas_textos,bd=0,width=12,font=("Arial",14))
        self.horarios_texto.pack()
        #FIN CAJITA DE TEXTOS


        #CAJITA DE BOTONES
        self.cajas_botones=LabelFrame(self,text="Cajas de botones",width=150,height=430,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_botones.grid(row=0,column=1,pady=20,padx=20)

        #boton nuevo
        self.nuevo=Button(self.cajas_botones,command=lambda:f_nuevo(self),text="Nuevo",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        #boton actualizar
        self.actualizar=Button(self.cajas_botones,command=lambda:f_actualizar(self),text="Actualizar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        #boton eliminar
        self.eliminar=Button(self.cajas_botones,command=lambda:f_eliminar(self),text="Eliminar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)

        #boton cancelar
        self.cancelar=Button(self.cajas_botones,command=lambda:f_limpiar(self),text="Cancelar",bg=COLOR_BOTON,fg="White",relief=FLAT,bd=0,width=20,height=2,font=("Arial",10)).pack(pady=10)
        #FIN CAJITA DE BOTONES


        #CAJA DE TABLA DE DATOS
        self.cajas_datos=LabelFrame(self,text="Lista de tareas",width=600,height=360,bg=COLOR_FONDO_PRIMARIO,fg="white",font=("arial",12),relief=FLAT,pady=60)
        self.cajas_datos.grid(row=0,column=2,pady=20,padx=20)
        # tabla
        self.tabla_datos=ttk.Treeview(self.cajas_datos,columns=("#1","#2"))
        self.tabla_datos.column("#0",width=40)
        self.tabla_datos.column("#1",width=120)
        self.tabla_datos.column("#2",width=40)

        self.tabla_datos.heading("#0",text="Nombres")
        self.tabla_datos.heading("#1",text="actividades")
        self.tabla_datos.heading("#2",text="horarios")
        personas=[
            ("liz","jugar voley","8:00-9:00pm"),
            ("luis","hacer deportes","6:00-7:00pm"),
            ("maria","leer libros","9:30-10:00pm"),
            ("maritza","investigar sobre un problema","7:00-8:00pm"),
        ]
        for nom,acti,hora in personas:
            self.tabla_datos.insert("",END,text=nom,values=(acti,hora))
        self.tabla_datos.bind("<Double-1>",lambda event:f_dobleClick(self,event))

        self.tabla_datos.place(x=0,y=0,width=400,height=600)
        
        # FIN DE TABLA DE DATOS