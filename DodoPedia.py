import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

ARCHIVO = "D:\\3IV7-González-Cardoso-René\\Python\\Examen2\\dodopedia.txt"

criaturas = []

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            next(f)  
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 8:
                    criatura = {
                        "nombre": partes[0],
                        "mapa": partes[1],
                        "tipo": partes[2],
                        "metodo_de_tameo": partes[3],
                        "salud": partes[4],
                        "daño": partes[5],
                        "velocidad": partes[6],
                        "resistencia": partes[7]
                    }
                    criaturas.append(criatura)

def buscar_criatura():
    nombre = simpledialog.askstring("Buscar Criatura", "Nombre de la criatura a buscar:")
    for criatura in criaturas:
        if criatura['nombre'].lower() == nombre.lower():
            detalles = (
                f"Nombre: {criatura['nombre']}\n"
                f"Mapa: {criatura['mapa']}\n"
                f"Tipo: {criatura['tipo']}\n"
                f"Método de Tameo: {criatura['metodo_de_tameo']}\n"
                f"Salud: {criatura['salud']}\n"
                f"Daño: {criatura['daño']}\n"
                f"Velocidad: {criatura['velocidad']}\n"
                f"Resistencia: {criatura['resistencia']}"
            )
            messagebox.showinfo("Detalles de Criatura", detalles)
            return
    messagebox.showwarning("No Encontrado", "No se encontró ninguna criatura con ese nombre.")

def registrar_criatura():
    nombre = simpledialog.askstring("Entrada", "Nombre de la criatura:")
    mapa = simpledialog.askstring("Entrada", "Mapa donde se encuentra:")
    tipo = simpledialog.askstring("Entrada", "Tipo de criatura:")
    metodo_de_tameo = simpledialog.askstring("Entrada", "Método de tameo (Pasiva/Derribo):")
    salud = simpledialog.askstring("Entrada", "Salud:")
    daño = simpledialog.askstring("Entrada", "Daño:")
    velocidad = simpledialog.askstring("Entrada", "Velocidad:")
    resistencia = simpledialog.askstring("Entrada", "Resistencia:")
    
    criatura = {
        "nombre": nombre,
        "mapa": mapa,
        "tipo": tipo,
        "metodo_de_tameo": metodo_de_tameo,
        "salud": salud,
        "daño": daño,
        "velocidad": velocidad,
        "resistencia": resistencia
    }
    criaturas.append(criatura)
    guardar_datos()
    messagebox.showinfo("Éxito", "Criatura registrada exitosamente.")

def mostrar_tabla_criaturas():
    ventana_lista = tk.Toplevel()
    ventana_lista.title("Lista de Criaturas")
    ventana_lista.geometry("850x450")

    titulo = tk.Label(ventana_lista, text="Lista de Criaturas Registradas", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    frame_tabla = tk.Frame(ventana_lista)
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar_y = ttk.Scrollbar(frame_tabla, orient="vertical")
    scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal")

    tabla = ttk.Treeview(
        frame_tabla,
        columns=("nombre", "mapa", "tipo", "metodo_de_tameo", "salud", "daño", "velocidad", "resistencia"),
        show="headings",
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    tabla.heading("nombre", text="Nombre")
    tabla.heading("mapa", text="Mapa")
    tabla.heading("tipo", text="Tipo")
    tabla.heading("metodo_de_tameo", text="Método de Tameo")
    tabla.heading("salud", text="Salud")
    tabla.heading("daño", text="Daño")
    tabla.heading("velocidad", text="Velocidad")
    tabla.heading("resistencia", text="Resistencia")

    tabla.column("nombre", width=100)
    tabla.column("mapa", width=100)
    tabla.column("tipo", width=100)
    tabla.column("metodo_de_tameo", width=120)
    tabla.column("salud", width=80)
    tabla.column("daño", width=80)
    tabla.column("velocidad", width=80)
    tabla.column("resistencia", width=80)

    scrollbar_y.config(command=tabla.yview)
    scrollbar_x.config(command=tabla.xview)

    tabla.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")

    frame_tabla.grid_rowconfigure(0, weight=1)
    frame_tabla.grid_columnconfigure(0, weight=1)

    for criatura in criaturas:
        tabla.insert("", "end", values=(
            criatura['nombre'], 
            criatura['mapa'], 
            criatura['tipo'], 
            criatura['metodo_de_tameo'], 
            criatura['salud'], 
            criatura['daño'], 
            criatura['velocidad'], 
            criatura['resistencia']
        ))

def editar_criatura():
    nombre = simpledialog.askstring("Editar Criatura", "Nombre de la criatura a editar:")
    for criatura in criaturas:
        if criatura['nombre'].lower() == nombre.lower():
            criatura['mapa'] = simpledialog.askstring("Editar", "Mapa:", initialvalue=criatura['mapa']) or criatura['mapa']
            criatura['tipo'] = simpledialog.askstring("Editar", "Tipo:", initialvalue=criatura['tipo']) or criatura['tipo']
            criatura['metodo_de_tameo'] = simpledialog.askstring("Editar", "Método de Tameo:", initialvalue=criatura['metodo_de_tameo']) or criatura['metodo_de_tameo']
            criatura['salud'] = simpledialog.askstring("Editar", "Salud:", initialvalue=criatura['salud']) or criatura['salud']
            criatura['daño'] = simpledialog.askstring("Editar", "Daño:", initialvalue=criatura['daño']) or criatura['daño']
            criatura['velocidad'] = simpledialog.askstring("Editar", "Velocidad:", initialvalue=criatura['velocidad']) or criatura['velocidad']
            criatura['resistencia'] = simpledialog.askstring("Editar", "Resistencia:", initialvalue=criatura['resistencia']) or criatura['resistencia']
            guardar_datos()
            messagebox.showinfo("Éxito", "Criatura editada exitosamente.")
            return
    messagebox.showwarning("Error", "Criatura no encontrada.")

def eliminar_criatura():
    nombre = simpledialog.askstring("Eliminar Criatura", "Nombre de la criatura a eliminar:")
    for criatura in criaturas:
        if criatura['nombre'].lower() == nombre.lower():
            criaturas.remove(criatura)
            guardar_datos()
            messagebox.showinfo("Éxito", "Criatura eliminada exitosamente.")
            return
    messagebox.showwarning("Error", "Criatura no encontrada.")

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        f.write("nombre,mapa,tipo,metodo_de_tameo,salud,daño,velocidad,resistencia\n")
        for criatura in criaturas:
            f.write(f"{criatura['nombre']},{criatura['mapa']},{criatura['tipo']},{criatura['metodo_de_tameo']},{criatura['salud']},{criatura['daño']},{criatura['velocidad']},{criatura['resistencia']}\n")

def main():
    cargar_datos()
    global root
    root = tk.Tk()
    root.title("DodoPedia")
    
    tk.Button(root, text="Registrar Criatura", command=registrar_criatura).pack(pady=5)
    tk.Button(root, text="Listar Criaturas", command=mostrar_tabla_criaturas).pack(pady=5)
    tk.Button(root, text="Buscar Criatura", command=buscar_criatura).pack(pady=5)
    tk.Button(root, text="Editar Criatura", command=editar_criatura).pack(pady=5)
    tk.Button(root, text="Eliminar Criatura", command=eliminar_criatura).pack(pady=5)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=5)
    
    root.mainloop()

main()
