from model.model import Model
from view.view import View
from datetime import date
from datetime import datetime

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.init_menu()

    def init_menu(self):
        o = '0'
        while o != '3':
            self.view.init_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.usuarios_funciones_menu()
            elif o == '2':
                self.administradores_login()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f, v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals
    
    """
    ***************************
    * Control para el usuario *
    ***************************
    """

    def usuarios_funciones_menu(self):
        o = '0'
        while o != '6':
            self.view.usuarios_funciones_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_a_funcion()
            elif o == '2':
                self.read_all_funciones()
            elif o == '3':
                self.read_funciones_fecha()
            elif o == '4':
                self.read_funciones_tituloPelicula()
            elif o == '5':
                self.comprar_boleto()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def read_a_funcion(self):
        self.view.ask('ID funcion: ')
        idFuncion = input()
        funcion = self.model.read_a_funcion(idFuncion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de las funcion '+idFuncion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_footer()
        else:
            if idFuncion == None:
                self.view.error('LA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA')
        return

    def read_all_funciones(self):
        funciones = self.model.read_all_funciones()
        if type(funciones) == list:
            self.view.show_funcion_header(' Datos de todas las funciones ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funciones_fecha(self):
        self.view.ask('Fecha (yyyy/mm/dd): ')
        fecha = input()
        funciones = self.model.read_funiones_fecha(fecha)
        if type(funciones) == list:
            self.view.show_funcion_header(' Datos de todas las funciones ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return
    
    def read_funciones_tituloPelicula(self):
        self.view.ask('Titulo de la pelicula: ')
        tituloPelicula = input()
        funciones = self.model.read_pelicula_nombre(tituloPelicula)
        if type(funciones) == list:
            self.view.show_funcion_header(' Datos de la funcion: ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def comprar_boleto(self):
        o = '0'
        while o != '5':
            self.view.compra_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.create_usuario()
            elif o == '2':
                self.create_boleto()
            elif o == '3':
                self.read_a_boleto()
            elif o == '4':
                self.ticket_menu()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return


    """
    *********************************
    * Control para el administrador *
    *********************************
    """
    def administradores_login(self):
        o = '0'
        while o != '3':
            self.view.administradores_login()
            self.view.option('3')
            o = input()
            if o == '1':
                if self.inicio_sesion() == True:
                    self.menu_administrador()
            elif o == '2':
                if self.nuevo_adminstrador() == True:
                    self.menu_administrador()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admi(self):
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        aPaterno = input()
        self.view.ask('Apellido Materno: ')
        aMaterno = input()
        self.view.ask('Correo: ')
        correo = input()
        return [usuario, contrasena, nombre, aPaterno, aMaterno, correo]

    def inicio_sesion(self):
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contrasena = input()
        admi = self.model.read_administrador_usuario_contrasena(usuario, contrasena)
        if type(admi) == tuple:
            return True
        else:
            if admi == None:
                self.view.error('USUARIO Y/O CONTRASEÑA MAL. REVISA')
            else:
                self.view.error('PROBLEMA AL VALIDAR ADMINISTRADOR')
        return
    
    def nuevo_adminstrador(self):
        usuario, contrasena, nombre, aPaterno, aMaterno, correo = self.ask_admi()
        out = self.model.create_administrador(usuario, contrasena, nombre, aPaterno, aMaterno, correo)
        if out == True:
            self.view.ok(nombre+' '+aPaterno+' '+aMaterno, 'agrego')
            return True
        else:
            self.view.error('NO SE PUDO CREAR EL ADMINISTRADOR. REVISA.')
        return

    def menu_administrador(self):
        o = '0'
        while o != '9':
            self.view.menu_administrador()
            self.view.option('9')
            o = input()
            if o == '1':
                self.administradores_menu()
            elif o == '2':
                self.usuarios_menu()
            elif o == '3':
                self.peliculas_menu()
            elif o == '4':
                self.salas_menu()
            elif o == '5':
                self.funciones_menu()
            elif o == '6':
                self.asientos_menu()
            elif o == '7':
                self.boletos_menu()
            elif o == '8':
                self.ticket_menu()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return
    
    """
    ********************************
    * Control para administradores *
    ********************************
    """

    def administradores_menu(self):
        o = '0'
        while o != '6':
            self.view.administradores_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_administrador()
            elif o == '2':
                self.read_a_administrador()
            elif o == '3':
                self.read_all_administradores()
            elif o == '4':
                self.update_administrador()
            elif o == '5':
                self.delete_administrador()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def create_administrador(self):
        usuario, contrasena, nombre, aPaterno, aMaterno, correo = self.ask_admi()
        out = self.model.create_administrador(usuario, contrasena, nombre, aPaterno, aMaterno, correo)
        if out == True:
            self.view.ok(nombre+' '+aPaterno+' '+aMaterno, 'agrego')
        else:
            self.view.error('NO SE PUDO CARGAR EL ADMINISTRADOR. REVISA.')
        return
    
    def read_a_administrador(self):
        self.view.ask('ID administrador: ')
        idAdministrador = input()
        administrador = self.model.read_a_administrador(idAdministrador)
        if type(administrador) == tuple:
            self.view.show_administrador_header(' Datos del administrador '+idAdministrador+' ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if idAdministrador == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        return

    def read_all_administradores(self):
        administradores = self.model.read_all_administradores()
        if type(administradores) == list:
            self.view.show_administrador_header(' Todos los administradores ')
            for administrador in administradores:
                self.view.show_a_administrador(administrador)
                self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINISTRADORES. REVISA')
        return

    def update_administrador(self):
        self.view.ask('ID del administrador a modificar: ')
        idAdministrador = input()
        admi = self.model.read_a_administrador(idAdministrador)
        if type(admi) == tuple:
            self.view.show_administrador_header(' Datos del cliente ')
            self.view.show_a_administrador(admi)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if admi == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_admi()
        fields, vals = self.update_lists(['a_Usuario','a_Contrasena', 'a_Nombre', 'a_APaterno', 'a_AMaterno', 'a_Correo'], whole_vals)
        vals.append(idAdministrador)
        vals = tuple(vals)
        out = self.model.update_administrador(fields, vals)
        if out == True:
            self.view.ok(idAdministrador, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA.')
        return

    def delete_administrador(self):
        self.view.ask('ID del administrador a borrar: ')
        idAdministrador = input()
        count = self.model.delete_administrador(idAdministrador)
        if count != 0:
            self.view.ok(idAdministrador, 'borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL ADMINISTRADOR')
        return

    """
    *************************
    * Control para usuarios *
    *************************
    """
    def usuarios_menu(self):
        o = '0'
        while o != '6':
            self.view.usuarios_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_usuario()
            elif o == '2':
                self.read_a_usuario()
            elif o == '3':
                self.read_all_usuarios()
            elif o == '4':
                self.update_usuario()
            elif o == '5':
                self.delete_usuario()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return
    
    def create_usuario(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        aPaterno = input()
        self.view.ask('Apellido Materno: ')
        aMaterno = input()
        self.view.ask('Correo: ')
        correo = input()
        out = self.model.create_usuario(nombre, aPaterno, aMaterno, correo)
        if out == True:
            self.view.ok(nombre+' '+aPaterno+' '+aMaterno, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return
    
    def read_a_usuario(self):
        self.view.ask('ID usuario: ')
        idUsuario = input()
        usuario = self.model.read_a_usuario(idUsuario)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+idUsuario+' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if idUsuario == None:
                self.view.error('EL USUARIO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return

    def read_all_usuarios(self):
        usuarios = self.model.read_all_usuarios()
        if type(usuarios) == list:
            self.view.show_usuario_header(' Todos los usuarios ')
            for usuario in usuarios:
                self.view.show_a_usuario(usuario)
                self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS USUARIOS. REVISA')
        return

    def update_usuario(self):
        self.view.ask('ID de usario a modificar: ')
        idUsuario = input()
        usuario = self.model.read_a_usuario(idUsuario)
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+idUsuario+' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PRIBLEMA AL LEER EL USUARIO. REVISE.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        aPaterno = input()
        self.view.ask('Apellido Materno: ')
        aMaterno = input()
        self.view.ask('Correo: ')
        correo = input()
        whole_vals = [nombre, aPaterno, aMaterno, correo]
        fields, vals = self.update_lists(['u_Nombre', 'u_APaterno', 'u_AMaterno', 'u_Correo'], whole_vals)
        vals.append(idUsuario)
        vals = tuple(vals)
        out = self.model.update_usuario(fields, vals)
        if out == True:
            self.view.ok(idUsuario, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISE')
        return

    def delete_usuario(self):
        self.view.ask('ID del usuario a borrar: ')
        idUsuario = input()
        count = self.model.delete_usuario(idUsuario)
        if count != 0:
            self.view.ok(idUsuario, 'borro')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL USUARIO. REVISE')
        return
    
    """
    *************************
    * Control para peliculas *
    *************************
    """
    def peliculas_menu(self):
        o = '0'
        while o != '9':
            self.view.peliculas_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_pelicula()
            elif o == '2':
                self.read_a_pelicula()
            elif o == '3':
                self.read_all_peliculas()
            elif o == '4':
                self.read_pelicula_nombre()
            elif o == '5':
                self.read_peliculas_genero()
            elif o == '6':
                self.read_peliculas_clasificacion()
            elif o == '7':
                self.update_pelicula()
            elif o == '8':
                self.delete_pelicula()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_pelicula(self):
        self.view.ask('Titulo: ')
        tituloPelicula = input()
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        self.view.ask('Genero: ')
        genero = input()
        self.view.ask('Duracion: ')
        duracion = input()
        return [tituloPelicula, clasificacion, genero, duracion]

    def create_pelicula(self):
        tituloPelicula, clasificacion, genero, duracion = self.ask_pelicula()
        out = self.model.create_pelicula(tituloPelicula, clasificacion, genero, duracion)
        if out == True:
            self.view.ok(tituloPelicula+' '+clasificacion+' '+genero, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return
    
    def read_a_pelicula(self):
        self.view.ask('ID pelicula: ')
        idPelicula = input()
        pelicula = self.model.read_a_pelicula(idPelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+idPelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if idPelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Todos las Peliculas ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_pelicula_nombre(self):
        self.view.ask('Titulo de la pelicula: ')
        tituloPelicula = input()
        pelicula = self.model.read_pelicula_nombre(tituloPelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Pelicula con el nombre: '+tituloPelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return
    
    def read_peliculas_genero(self):
        self.view.ask('Genero: ')
        genero = input()
        peliculas = self.model.read_peliculas_genero(genero)
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Peliculas con el genero: '+genero+' ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return

    def read_peliculas_clasificacion(self):
        self.view.ask('Clasificacion: ')
        clasificacion = input()
        peliculas = self.model.read_peliculas_clasificacion(clasificacion)
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Peliculas con clasificacion: '+clasificacion+' ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return

    def update_pelicula(self):
        self.view.ask('ID de pelicula a modificar: ')
        idPelicula = input()
        pelicula = self.model.read_a_pelicula(idPelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+idPelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISE.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['p_TituloPelicula', 'p_Clasificacion', 'p_Genero', 'p_Duracion'], whole_vals)
        vals.append(idPelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields, vals)
        if out == True:
            self.view.ok(idPelicula, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISE.')
        return

    def delete_pelicula(self):
        self.view.ask('ID de la pelicula a borrar: ')
        idPelicula = input()
        count = self.model.delete_pelicula(idPelicula)
        if count != 0:
            self.view.ok(idPelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISE.')
        return

    """
    **********************
    * Control para salas *
    **********************
    """
    def salas_menu(self):
        o = '0'
        while o != '6':
            self.view.salas_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_salas()
            elif o == '4':
                self.update_sala()
            elif o == '5':
                self.delete_sala()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def create_sala(self):
        self.view.ask('Numéro de pasillos: ')
        noPasillos = input()
        self.view.ask('Numero de asientos: ')
        noAsientos = input()
        out = self.model.create_sala(noPasillos, noAsientos)
        if out == True:
            self.view.ok(out, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA.')
        return

    def read_a_sala(self):
        self.view.ask('Numero de sala: ')
        noSala = input()
        sala = self.model.read_a_sala(noSala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+noSala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if noSala == None:
                self.view.error('LA SALA NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        return

    def read_all_salas(self):
        salas = self.model.read_all_salas()
        if type(salas) == list:
            self.view.show_sala_header(' Todos las salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA')
        return

    def update_sala(self):
        self.view.ask('Numero de sala a modificar: ')
        noSala = input()
        sala = self.model.read_a_sala(noSala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+noSala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PRIBLEMA AL LEER LA SALA. REVISE.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        self.view.ask('Numero de pasillos: ')
        noPasillos = input()
        self.view.ask('Numero de asientos: ')
        noAsientos = input()
        whole_vals = [noPasillos, noAsientos]
        fields, vals = self.update_lists(['s_NoPasillos', 's_NoAsientos'], whole_vals)
        vals.append(noSala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(noSala, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISE')
        return

    def delete_sala(self):
        self.view.ask('Numero de sala a borrar: ')
        noSala = input()
        count = self.model.delete_sala(noSala)
        if count != 0:
            self.view.ok(noSala, 'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISE')
        return

    """
    **************************
    * Control para funciones *
    **************************
    """
    def funciones_menu(self):
        o = '0'
        while o != '8':
            self.view.funciones_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_funcion()
            elif o == '2':
                self.read_a_funcion()
            elif o == '3':
                self.read_all_funciones()
            elif o == '4':
                self.read_funciones_fecha()
            elif o == '5':
                self.read_funciones_tituloPelicula()
            elif o == '6':
                self.update_funcion()
            elif o == '7':
                self.delete_funcion()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return
    
    def create_funcion(self):
        self.view.ask('ID de la pelicula: ')
        idPelicula = input()
        self.view.ask('Numero de la sala: ')
        noSala = input()
        today = date.today()
        fecha = today.strftime('%y-%m-%d')
        self.view.ask('Hora de la función (HH:MM): ')
        hora = input()
        out = self.model.create_funcion(idPelicula, noSala, fecha, hora)
        if out == True:
            self.view.ok(idPelicula, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISE.')
        return

    def update_funcion(self):
        self.view.ask('ID funcion a modificar: ')
        idFuncion = input()
        funcion = self.model.read_a_funcion(idFuncion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de todas la funcion ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISE')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual)')
        self.view.ask('ID de la pelicula: ')
        idPelicula = input()
        self.view.ask('Numero de la sala: ')
        noSala = input()
        today = date.today()
        fecha = today.strftime('%y-%m-%d')
        self.view.ask('Hora de la función (HH:MM): ')
        hora = input()
        whole_vals = [idPelicula, noSala, fecha, hora]
        fields, vals = self.update_lists(['f_idPelicula', 'f_noSala', 'f_fecha', 'f_Hora'], whole_vals)
        vals.append(idFuncion)
        vals = tuple(vals)
        out = self.model.update_funcion(fields, vals)
        if out == True:
            self.view.ok(idFuncion, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTALIZAR LA FUNCION. REVISE')
        return

    def delete_funcion(self):
        self.view.ask('ID funcion a eliminar')
        idFuncion = input()
        count = self.model.delete_funcion(idFuncion)
        if count != 0:
            self.view.ok(idFuncion, 'borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA LA LEER LA FUNCION. REVISE')
        return
    """
    *************************
    * Control para asientos *
    *************************
    """
    def asientos_menu(self):
        o = '0'
        while o != '6':
            self.view.asientos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_asiento()
            elif o == '2':
                self.read_a_asiento()
            elif o == '3':
                self.read_all_asientos()
            elif o == '4':
                self.update_asiento()
            elif o == '5':
                self.delete_asiento()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def create_asiento(self):
        self.view.ask('Numero de sala: ')
        noSala = input()
        self.view.ask('Numero de asiento: ')
        noAsiento = input()
        estado = 'libre'
        out = self.model.create_asiento(noSala, noAsiento, estado)
        if out == True:
            self.view.ok(noAsiento, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA.')
        return

    def read_a_asiento(self):
        self.view.ask('ID Asiento: ')
        idAsiento = input()
        asiento = self.model.read_a_asiento(idAsiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos del asiento '+idAsiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if idAsiento == None:
                self.view.error('El ASIENTO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return

    def read_all_asientos(self):
        asientos = self.model.read_all_asietos()
        if type(asientos) == list:
            self.view.show_asiento_header(' Todos los asientos ')
            for asiento in asientos:
                self.view.show_a_asiento(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA')
        return

    def update_asiento(self):
        self.view.ask('ID asiento a modificar: ')
        idAsiento = input()
        asiento = self.model.read_a_asiento(idAsiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos del asiento '+idAsiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('El ASIENTO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        self.view.ask('Numero de sala: ')
        noSala = input()
        self.view.ask('Numero de asiento: ')
        noAsiento = input()
        self.view.ask('Estado (ocupado o libre): ')
        estado = input()
        whole_vals = [noSala, noAsiento, estado]
        fields, vals = self.update_lists(['asi_noSala', 'asi_NoAsiento', 'asi_estado'], whole_vals)
        vals.append(idAsiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields, vals)
        if out == True:
            self.view.ok(idAsiento, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO5. REVISE')
        return

    def delete_asiento(self):
        self.view.ask('ID asiento a borrar: ')
        idAsiento = input()
        count = self.model.delete_asiento(idAsiento)
        if count != 0:
            self.view.ok(idAsiento, 'borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISE')
        return

    """
    ************************
    * Control para boletos *
    ************************
    """        
    def boletos_menu(self):
        o = '0'
        while o != '6':
            self.view.boletos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_boleto()
            elif o == '2':
                self.read_a_boleto()
            elif o == '3':
                self.read_all_boletos()
            elif o == '4':
                self.update_boleto()
            elif o == '5':
                self.delete_boleto()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_boleto(self):
        self.view.ask('ID funcion: ')
        idFuncion = input()
        self.view.ask('ID asiento: ')
        idAsiento = input()
        self.view.ask('ID pelicula: ')
        idPelicula = input()
        self.view.ask('Numero de sala: ')
        noSala = input()
        return [idFuncion, idAsiento, idPelicula, noSala]

    def create_boleto(self):
        precio = 69.99
        idFuncion, idAsiento, idPelicula, noSala = self.ask_boleto()
        out = self.model.create_boleto(idFuncion, idAsiento, idPelicula, noSala, precio)
        if out == True:
            self.view.ok(idFuncion+' '+idAsiento+' '+idPelicula, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA.')
        return

    def read_a_boleto(self):
        self.view.ask('ID boleto: ')
        idBoleto = input()
        boleto = self.model.read_a_boleto(idBoleto)
        if type(boleto) == tuple:
            self.view.show_boleto_header(' Datos del boleto'+idBoleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if idBoleto == None:
                self.view.error('El BOLETO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        return

    def read_all_boletos(self):
        boletos = self.model.read_all_boletos()
        if type(boletos) == list:
            self.view.show_boleto_header(' Todos los boletos ')
            for boleto in boletos:
                self.view.show_a_boleto(boleto)
                self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS. REVISA')
        return

    def update_boleto(self):
        self.view.ask('ID boleto a modificar: ')
        idBoleto = input()
        boleto = self.model.read_a_boleto(idBoleto)
        if type(boleto) == tuple:
            self.view.show_asiento_header(' Datos del boleto '+idBoleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('El BOLETO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        self.view.ask('Precio: ')
        precio = input()
        whole_vals = self.ask_boleto()
        whole_vals.append(precio)
        fields, vals = self.update_lists(['b_idFuncion', 'b_idAsiento', 'b_idPelicula', 'b_nosala', 'b_Precio'], whole_vals)
        vals.append(idBoleto)
        vals = tuple(vals)
        out = self.model.update_boleto(fields, vals)
        if out == True:
            self.view.ok(idBoleto, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL BOLETO. REVISE')
        return

    def delete_boleto(self):
        self.view.ask('ID boleto a borrar: ')
        idBoleto = input()
        count = self.model.delete_boleto(idBoleto)
        if count != 0:
            self.view.ok(idBoleto, 'borro')
        else:
            if count == 0:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL BOLETO. REVISE')
        return

    """
    ************************
    * Control para tickets *
    ************************
    """     
    def ticket_menu(self):
        o = '0'
        while o != '8':
            self.view.ticket_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_ticket()
            elif o == '2':
                self.read_a_ticket()
            elif o == '3':
                self.read_all_ticket()
            elif o == '4':
                self.update_ticket()
            elif o == '5':
                self.add_detalleVentaBoleto()
            elif o == '6':
                self.delete_detalleVentaBoleto()
            elif o == '7':
                self.delete_ticket()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def create_ticket(self):      
        self.view.ask('ID usuario: ')
        idUsuario = input()
        today = date.today()
        fecha = today.strftime('%y-%m-%d')
        hora = datetime.now()
        total = 0.0
        idTicket = self.model.create_ticket(idUsuario, fecha, hora, total)
        if type(idTicket) == int:
            idBoleto = ' '
            while idBoleto != ' ':
                self.view.msg('--- Agregar boletos al ticket (deje vacio el id del boleto para salir) ---')
                idBoleto, totalBoletos = self.create_detalleVentaBoleto(idTicket)
                total += totalBoletos
            self.model.update_ticket(('t_Total = %s'),(total, idTicket))
        else:
            self.view.error('NO SE PUDO CREAR UN TICKET. REVISE')
        return

    def read_a_ticket(self):
        self.view.ask('ID ticket: ')
        idTicket = input()
        ticket = self.model.read_a_ticket(idTicket)
        if type(ticket) == tuple:
            detalleVentaBoletos = self.model.read_detalleVentaBoleto(idTicket)
            if type(detalleVentaBoletos) != list and detalleVentaBoletos != None:
                self.view.error('PROBLEMA AL LEER UN TICKET. REVISE.')
            else:
                self.view.show_ticket_header(' Datos del ticket '+idTicket)
                self.view.show_ticket(ticket)
                self.view.show_detalleVentaBoleto_header(' Detalle del ticket ')
                for detalleVentaBoleto in detalleVentaBoletos:
                    self.view.show_detalleVentaBoleto(detalleVentaBoleto)
                    self.view.show_detalleVentaBoleto_midder()
                self.view.show_detalleVentaBoleto_footer()
                self.view.show_ticket_total(ticket)
                self.view.show_ticket_footer()
                return ticket
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL TICKET. REVISE.')
        return

    def read_all_ticket(self):
        tickets = self.model.read_all_ticket()
        if type(tickets) == list:
            self.view.show_ticket_header(' Todos los tickets ')
            for ticket in tickets:
                idTicket = tickets[0]
                detalleVentaBoletos = self.model.read_detalleVentaBoleto(idTicket)
                if type(detalleVentaBoletos) != list and detalleVentaBoletos != None:
                    self.view.error('PROBLEMA AL LEER EL TICKET REVISE. ')
                else:
                    self.view.show_ticket(ticket)
                    self.view.show_detalleVentaBoleto_header(' Detalle del ticket ')
                    for detalleVentaBoleto in detalleVentaBoletos:
                        self.view.show_detalleVentaBoleto(detalleVentaBoleto)
                        self.view.show_detalleVentaBoleto_midder()
                    self.view.show_detalleVentaBoleto_footer()
                    self.view.show_ticket_total(ticket)
                    self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS TICKET. REVISE.')
        return
    
    def update_ticket(self):
        self.view.ask('ID ticket a modificar: ')
        idTicket = input()
        ticket = self.model.read_a_ticket(idTicket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+idTicket)
            self.view.show_ticket(ticket)
            self.view.show_ticket_total(ticket)
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL TICKET. REVISE.')
            return
        self.view.msg('Ingrese los valores a modificar (vacio para dejar igual): ')
        self.view.ask('ID Usuario: ')
        idUsuario = input()
        self.view.ask('Fecha (aaaa/mm/dd): ')
        fecha = input()
        whole_vals = [idUsuario, fecha]
        fields, vals = self.update_lists(['t_idUsuario', 't_Fecha'], whole_vals)
        vals.append(idTicket)
        vals = tuple(vals)
        out = self.model.update_ticket(fields, vals)
        if out == True:
            self.view.ok(idTicket, 'actualizado')
        else:
             self.view.error('NO SE PUDO ACTUALIZAR EL TICKET. REVISE.')
        return
    
    def delete_ticket(self):
        self.view.ask('ID del ticket a borrar: ')
        idTicket = input()
        count = self.model.delete_ticket(idTicket)
        if count != 0:
            self.view.ok(idTicket, 'borro')
        else:
            if count == 0:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL TICKET. REVISE.')
        return
    
    """
    ************************
    * Control para tickets *
    ************************
    """
    def create_detalleVentaBoleto(self, idTicket):
        totalBoletos = 0.0
        self.view.ask('ID boleto: ')
        idBoleto = input()
        if idBoleto != '':
            boleto = self.model.read_a_boleto(idBoleto)
            if type(boleto) == tuple:
                self.view.show_boleto_header('Datos del boleto '+idBoleto+' ')
                self.view.show_a_boleto(boleto)
                self.view.show_boleto_footer()
                self.view.ask('Cantidad: ')
                cantidad = input()
                totalBoletos = float(cantidad)*boleto[6]
                out = self.model.create_detalleVentaBoleto(idBoleto, idTicket, cantidad, totalBoletos)
                if out == True:
                    self.view.ok(idBoleto, 'agrego al ticket')
                else:
                    if out.errno == 1062:
                        self.view.error('EL BOLETO YA ESTA EN LA ORDEN')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL BOLETO A LA ORDEN. REVISE.')
                    totalBoletos = 0.0
            else:
                if boleto == None:
                    self.view.error('EL BOLETO YA EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL BOLETO. REVISE.')
        return idBoleto, totalBoletos
    
    def add_detalleVentaBoleto(self):
        ticket = self.read_a_ticket()
        if type(ticket) == tuple:
            idTicket = ticket[0]
            total = ticket[5]
            idBoleto = ' '
            while idBoleto != '':
                self.view.msg('--- Agrega boletos al ticket (deja vacio el id del boleto para salir ---')
                idBoleto, totalBoletos = self.create_detalleVentaBoleto(idTicket)
                total += totalBoletos
            self.model.update_detalleVentaBoleto(('t_Total = %s'), (total, idTicket))
        return

    def delete_detalleVentaBoleto(self):
        ticket = self.read_a_ticket()
        if tuple(ticket) == tuple:
            idTicket = ticket[0]
            total = ticket[4]
            idBoleto = ' '
            while idBoleto != '':
                self.view.msg('--- Borra boletos del ticket (deja vacio el id del boleto para salir ---')
                self.view.ask('ID boleto: ')
                idBoleto = input()
                if idBoleto != '':
                    detalleVentaBoleto = self.model.read_a_detalleVentaBoleto(idBoleto, idTicket)
                    count = self.model.delete_detalleVentaBoleto(idBoleto, idTicket)
                    if type(detalleVentaBoleto) == tuple and count != 0:
                        totalBoletos = detalleVentaBoleto[3]
                        total -= totalBoletos
                        self.view.ok(idBoleto, 'borro del ticket')
                    else:
                        if detalleVentaBoleto == None:
                            self.view.error('EL BOLETO NO EXISTE EN LA TICKET')
                        else:
                            self.view.error('PROBLEMA AL BORRAR EL BOLETO. REVISE')
            self.model.update_ticket(('t_Total = %s'), (total, idTicket))
        return