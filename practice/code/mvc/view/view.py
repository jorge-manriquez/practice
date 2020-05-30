class View:
    def start(self):
        print('=================================')
        print('=      ¡Bienvenido al cine!     =')
        print('=================================')
    
    def end(self):
        print('=================================')
        print('=         Hasta la vista!       =')
        print('=================================')

    def init_menu(self):
        print('************************')
        print('* -- Menu Inicial -- *')
        print('************************')
        print('1. Usuario')
        print('2. Administrador')
        print('3. Salir')

    def administradores_login(self):
        print('********************')
        print('* -- Bienvenido -- *')
        print('********************')
        print('1. Inicie Sesión')
        print('2. Nuevo administrador')
        print('3. Regresar')
    
    def menu_administrador(self):
        print('*********************************')
        print('* -- Menu para Administrador -- *')
        print('*********************************')
        print('1. Administradores')
        print('2. Usuarios')
        print('3. Peliculas')
        print('4. Salas')
        print('5. Funciones')
        print('6. Asientos')
        print('7. Boletos')
        print('8. Ticket')
        print('9. Regresar')

    def option(self, last):
        print('Selecciona una opción (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opción no valida!\nIntente de nuevo')
    
    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ '+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ********************************
    *  Vistas para Administradores *
    ********************************
    """
    def administradores_menu(self):
        print('*********************************')
        print('* -- Submenu Administradores -- *')
        print('*********************************')
        print('1. Agregar administrador')
        print('2. Mostrar administrador')
        print('3. Mostrar todos los administradores')
        print('4. Actualizar aadministrador')
        print('5. Borrar administrador')
        print('6. Regresar')
    
    def show_a_administrador(self, record):
        print('ID: ', record[0])
        print('Usuario: ', record[1])
        print('Contraseña: ', record[2])
        print('Nombre:', record[3])
        print('Apellido paterno:', record[4])
        print('Apellido materno:', record[5])
        print('Correo:', record[6])

    def show_administrador_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_administrador_midder(self):
        print('-'*100)

    def show_administrador_footer(self):
        print('*'*100)

    """
    *************************
    *  Vistas para Usuarios *
    *************************
    """
    def usuarios_menu(self):
        print('**************************')
        print('* -- Submenu usuarios -- *')
        print('**************************')
        print('1. Agregar usuario')
        print('2. Mostrar usuario')
        print('3. Mostrar todos los usuarios')
        print('4. Actualizar cliente')
        print('5. Borrar usuario')
        print('6. Regresar')

    def show_a_usuario(self, record):
        print('ID: ', record[0])
        print('Nombre:', record[1])
        print('Apellido paterno:', record[2])
        print('Apellido materno:', record[3])
        print('Correo: ', record[4])

    def show_usuario_header(self, header):
        print(header.center(116,'*'))
        print('-'*100)
    
    def show_usuario_midder(self):
        print('-'*100)

    def show_usuario_footer(self):
        print('*'*100)
    
    """
    **************************
    *  Vistas para Peliculas *
    **************************
    """

    def peliculas_menu(self):
        print('**************************')
        print('* -- Submenu Peliculas -- *')
        print('**************************')
        print('1. Agregar pelicula')
        print('2. Mostrar pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por titulo')
        print('5. Mostrar peliculas por genero')
        print('6. Mostrar peliculas por clasificacion')
        print('7. Actualizar pelicula')
        print('8. Borrar pelicula')
        print('9. Regresar')
    
    def show_a_pelicula(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Clasificacion: ', record[2])
        print('Genero: ', record[3])
        print('Duracion: ', record[4])

    def show_pelicula_header(self, header):
        print(header.center(63,'*'))
        print('-'*63)

    def show_pelicula_midder(self):
        print('-'*63)
    
    def show_pelicula_footer(self):
        print('*'*63)

    """
    **********************
    *  Vistas para Salas *
    **********************
    """
    def salas_menu(self):
        print('*************************')
        print('* -- Submenu Salas -- *')
        print('*************************')
        print('1. Agregar sala')
        print('2. Mostrar sala')
        print('3. Mostrar todas las salas')
        print('4. Actualizar sala')
        print('5. Borrar sala')
        print('6. Regresar')
    
    def show_a_sala(self, record):
        print('ID: ', record[0])
        print('Numero de pasillos: ', record[1])
        print('Numero de asientos: ', record[2])

    def show_sala_header(self, header):
        print(header.center(10,'*'))
        print('-'*10)
    
    def show_sala_midder(self):
        print('-'*10)
    
    def show_sala_footer(self):
        print('*'*10)
    
    """
    **************************
    *  Vistas para Funciones *
    **************************
    """
    def funciones_menu(self):
        print('***************************')
        print('* -- Submenu Funciones -- *')
        print('***************************')
        print('1. Agregar una funcion')
        print('2. Mostrar una funcion')
        print('3. Mostrar todas las funciones')
        print('4. Mostrar funciones por fecha')
        print('5. Mostrar funciones por titulo de pelicula')
        print('6. Actualizar una funcion')
        print('7. Borrar una funcion')
        print('8. Regresar')

    def show_a_funcion(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Sala: ', record[2])
        print('Fecha: ', record[3])
        print('Hora: ', record[4])
    
    def show_funcion_header(self, header):
        print(header.center(90,'*'))
        print('-'*90)
        
        print('-'*90)
    
    def show_funcion_midder(self):
        print('-'*90)
    
    def show_funcion_footer(self):
        print('*'*90)
    
    """
    *************************
    *  Vistas para Asientos *
    *************************
    """
    def asientos_menu(self):
        print('**************************')
        print('* -- Submenu Asientos -- *')
        print('**************************')
        print('1. Agregar asiento')
        print('2. Mostrar asiento')
        print('3. Mostrar todos los asientos')
        print('4. Actualizar asiento')
        print('5. Borrar asiento')
        print('6. Regresar')

    def show_a_asiento(self, record):
        print('ID: ', record[0])
        print('Sala: ', record[1])
        print('Asiento: ', record[2])
        print('Estado:', record[3])
    
    def show_asiento_header(self, header):
        print(header.center(40,'*'))
        print('-'*40)

    def show_asiento_midder(self):
        print('-'*40)
    
    def show_asiento_footer(self):
        print('*'*40)

    """
    ************************
    *  Vistas para Boletos *
    ************************
    """

    def boletos_menu(self):
        print('*************************')
        print('* -- Submenu Boletos -- *')
        print('*************************')
        print('1. Agregar un boleto')
        print('2. Mostrar un boleto')
        print('3. Mostrar todos los boletos')
        print('4. Actualizar boleto')
        print('5. Borrar boleto')
        print('6, Regresar')

    def show_a_boleto(self, record):
        print('ID: ', record[0])
        print('Asiento: ', record[3])
        print('Titulo: ', record[4])
        print('Sala: ', record[5])
        print('Hora: ', record[2])
        print('Precio: ', record[6])
    
    def show_boleto_header(self, header):
        print(header.center(50,'*'))
        print('-'*50)

    def show_boleto_midder(self):
        print('-'*50)
    
    def show_boleto_footer(self):
        print('*'*50)

    """
    ************************
    *  Vistas para Ticket *
    ************************
    """

    def ticket_menu(self):
        print('*************************')
        print('* -- Submenu Tickets -- *')
        print('*************************')
        print('1. Agregar ticket')
        print('2. Mostrar un ticket')
        print('3. Mostrar todos los tickets')
        print('4. Actualizar ticket')
        print('5. Agregar boletos a un ticket')
        print('6. Borrar boletos de un ticket')
        print('7. Borrar ticket')
        print('8. Regresar')

    def show_ticket(self, record):
        print('ID: ', record[0])
        print('Fecha: ', record[3])
        print('Hora: ', record[4])
        print('Cliente:', record[1]+' '+record[2])

    def show_ticket_header(self, header):
        print(header.center(81,'+'))

    def show_ticket_midder(self):
        print('/'*81)

    def show_ticket_total(self, record):
        print('Total: '+str(record[5]))

    def show_ticket_footer(self):
        print('+'*81)

    """
    ***********************************
    *  Vistas para detalleVentaBoleto *
    ***********************************
    """
    def show_detalleVentaBoleto(self, record):
        print('ID: ', record[0])
        print('Funcion: ', record[1])
        print('Precio: ', record[2])
        print('Cantidad: ',record[3])
        print('Subtotal: ', record[4])
    
    def show_detalleVentaBoleto_header(self, header):
        print(header.center(70,'*'))
        print('-'*70)

    def show_detalleVentaBoleto_midder(self):
        print('-'*70)
    
    def show_detalleVentaBoleto_footer(self):
        print('*'*70)

    """
    ***********************************
    *  Vistas para Usuarios/Funciones *
    ***********************************
    """
    def usuarios_funciones_menu(self):
        print('***************************')
        print('* -- Submenu Funciones -- *')
        print('***************************')
        print('1. Mostrar una funcion')
        print('2. Mostrar todas las funciones')
        print('3. Mostrar funciones por fecha')
        print('4. Mostrar funciones por titulo de pelicula')
        print('5. Comprar un boleto')
        print('6. Regresar')

    def show_a_usuarios_funciones(self, record):
        print(f'{record[0]:<5}|{record[1]:<30]}|{record[2]:<5}|{record[3]:<12}|{record[4]:<10}')
    
    def show_usuarios_funciones_header(self):
        print('-'*90)
        print('ID'.ljust(5)+'|'+'Titulo pelicula'.ljust(30)+'|'+'Sala'.ljust(5)+'|'+'Fecha'.ljust(12)+'|'+'Hora'.ljust(10))
        print('-'*90)
    
    def show_usuarios_funciones_footer(self):
        print('-'*90)

    def compra_menu(self):
        print('***************************')
        print('* -- Submenu Compras -- *')
        print('***************************')
        print('1. Registrarse')
        print('2. Agregar boleto')
        print('3. Mostrar boleto')
        print('4. Menu ticket')
        print('5. Regresar')