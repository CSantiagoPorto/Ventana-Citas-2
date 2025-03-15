'''
Created on 5 mar 2025

@author: Iri
'''
import sys
import mysql.connector

from database import conectar, insertar

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox,\
    QTableWidgetItem
from PyQt6.QtCore import QDate
from ventana_citas import Ui_VentanaCitas

class VentanaPrincipal(QMainWindow, Ui_VentanaCitas):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.dateEdit.setMinimumDate(QDate.currentDate())  # Evita fechas anteriores a hoy
        self.dateEdit.setMinimumDate(QDate.currentDate())#Para que no deje seleccionar fechas anteriores

        self.btnAgregar.clicked.connect(self.agregar_cita) 
        
    def agregar_cita(self):
        #Obtenemos los datos
        nombre=self.leNombre.text()
        apellido=self.leApellido.text()
        telefono=self.leTlf.text()
        fecha= self.dateEdit.date().toString("yyyy-MM-dd")#Esto debería darle el formato correcto
            
        if nombre and apellido and telefono:#Si está todo colocamos los datos
            row_position =self.tabla.rowCount()
            self.tabla.insertRow(row_position)
            self.tabla.setItem(row_position,0,QTableWidgetItem(nombre))
            self.tabla.setItem(row_position,1,QTableWidgetItem(apellido))
            self.tabla.setItem(row_position,2,QTableWidgetItem(telefono))
            self.tabla.setItem(row_position,3,QTableWidgetItem(fecha))
            insertar(nombre,apellido,telefono, fecha)
                    
            self.leNombre.clear()
            self.leApellido.clear()
            self.leTlf.clear()
            self.dateEdit.setDate(QDate.currentDate())#Vuelve a la fecha ACTUAL
        else:
             QMessageBox.warning(self,"Error", "Hay campos vacíos")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())                    
                