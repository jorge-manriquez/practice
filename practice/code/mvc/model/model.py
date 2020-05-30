from mysql import connector

class Model():
        def __init__(self, config_db_file='config.txt'):
            self.config_db_file = config_db_file
            self.config_db_file = self.read_config_db()
            self.connect_to_db()

        def read_config_db(self):
            d = {}
            with open(self.config_db_file) as f_r:
                for line in f_r:
                    (key, val) = line.strip().split(':')
                    d[key] = val
            return d

        def connect_to_db(self):
            self.cnx = connector.connect(**self.config_db_file)
            self.cursor = self.cnx.cursor()

        def close_db(self):
            self.cnx.close()

        """
        Metodos administradores
        """
        def create_administrador(self, usuario, contrasena, nombre, aPaterno, aMaterno, correo):
            try:
                sql = 'INSERT INTO administradores (`a_Usuario`,`a_Contrasena`,`a_Nombre`,`a_APaterno`,`a_AMaterno`,`a_Correo`) VALUES (%s, %s, %s, %s, %s, %s)'
                vals = (usuario, contrasena, nombre, aPaterno, aMaterno, correo)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                #print(err)
                return err
        
        def read_a_administrador(self, idAdministrador):
            try:
                sql = 'SELECT * FROM administradores WHERE idAdministrador = %s'
                vals = (idAdministrador,)
                self.cursor.execute(sql, vals)
                record = self. cursor.fetchone()
                return record
            except connector.Error as err:
                print(err)
                return err

        def read_all_administradores(self):
            try:
                sql = 'SELECT * FROM administradores'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err

        def read_administrador_usuario_contrasena(self, usuario, contrasena):
            try:
                sql = 'SELECT a_Usuario, a_Contrasena FROM administradores WHERE a_Usuario = %s and a_Contrasena = %s'
                vals = (usuario, contrasena)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def update_administrador(self, fields, vals):
            try:
                sql = 'UPDATE administradores SET'+','.join(fields)+'WHERE idAdministrador = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err
        
        def delete_administrador(self, idAdministrador):
            try:
                sql = 'DELETE FROM administradores WHERE idAdministrador = %s'
                vals = (idAdministrador,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err

        """
        Metodos Usuarios
        """
        def create_usuario(self, nombre, aPaterno, aMaterno, correo):
            try:
                sql = 'INSERT INTO usuarios (`u_Nombre`, `u_APaterno`, `u_AMaterno`, `u_Correo`) VALUES (%s, %s, %s, %s)'
                vals = (nombre, aPaterno, aMaterno, correo)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err
        
        def read_a_usuario(self, idUsuario):
            try:
                sql = 'SELECT * FROM usuarios WHERE idUsuario = %s'
                vals = (idUsuario,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_all_usuarios(self):
            try:
                sql = 'SELECT * FROM usuarios'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def update_usuario(self, fields, vals):
            try:
                sql = 'UPDATE usuarios SET '+','.join(fields)+'WHERE idUsuario = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err
        
        def delete_usuario(self, idUsuario):
            try:
                sql = 'DELETE FROM usuarios WHERE idUsuario = %s'
                vals = (idUsuario,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        """
        Metodos Peliculas
        """
        def create_pelicula(self, tituloPelicula, clasificacion, genero, duracion):
            try:
                sql = 'INSERT INTO peliculas (`p_TituloPelicula`, `p_Clasificacion`, `p_Genero`, `p_Duracion`) VALUES (%s, %s, %s, %s)'
                vals = (tituloPelicula, clasificacion, genero, duracion)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def read_a_pelicula(self, idPelicula):
            try:
                sql = 'SELECT * FROM peliculas WHERE idPelicula = %s'
                vals = (idPelicula,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_all_peliculas(self):
            try:
                sql = 'SELECT * FROM peliculas'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def read_pelicula_nombre(self, tituloPelicula):
            try:
                sql = 'SELECT * FROM peliculas WHERE p_TituloPelicula = %s'
                vals = (tituloPelicula,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_peliculas_genero(self, genero):
            try:
                sql = 'SELECT * FROM peliculas WHERE p_Genero = %s'
                vals = (genero,)
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def read_peliculas_clasificacion(self, clasificacion):
            try:
                sql = 'SELECT * FROM peliculas WHERE p_Clasificacion = %s'
                vals = (clasificacion,)
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def update_pelicula(self, fields, vals):
            try:
                sql = 'UPDATE peliculas SET'+','.join(fields)+'WHERE idPelicula = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        def delete_pelicula(self, idPelicula):
            try:
                sql = 'DELETE FROM peliculas WHERE idPelicula = %s'
                vals = (idPelicula,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err

        """
        *************** Metodos Salas ***************
        """
        def create_sala(self, noPasillos, noAsientos):
            try:
                sql = 'INSERT INTO salas (`s_NoPasillos`, `s_NoAsientos`) VALUES (%s, %s)'
                vals = (noPasillos, noAsientos)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err

        def read_a_sala(self, noSala):
            try:
                sql = 'SELECT * FROM salas WHERE noSala = %s'
                vals = (noSala,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_all_salas(self):
            try:
                sql = 'SELECT * FROM salas'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err

        def update_sala(self, fields, vals):
            try:
                sql = 'UPDATE salas SET'+','.join(fields)+'WHERE noSala = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        def delete_sala(self, noSala):
            try:
                sql = 'DELETE FROM salas WHERE noSala = %s'
                vals = (noSala,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err

        """
        *************** Metodos funciones ***************
        """
        def create_funcion(self, idPelicula, noSala, fecha, hora):
            try:
                sql = 'INSERT INTO funciones (`f_idPelicula`, `f_noSala`, `f_fecha`, `f_Hora`) VALUES (%s, %s, %s, %s)'
                vals = (idPelicula, noSala, fecha, hora)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err

        def read_a_funcion(self, idFuncion):
            try:
                #sql = 'SELECT funciones.*, peliculas.*, salas.* FROM funciones JOIN peliculas ON peliculas.idPelicula = funciones.f_idPelicula and funciones.idFuncion = %s JOIN salas ON salas.noSala = funciones.f_noSala'
                sql = 'SELECT funciones.idFuncion, peliculas.p_TituloPelicula, salas.noSala, funciones.f_fecha, funciones.f_Hora FROM funciones JOIN peliculas ON peliculas.idPelicula = funciones.f_idPelicula and funciones.idFuncion = %s JOIN salas ON salas.noSala = funciones.f_noSala'
                vals = (idFuncion,)                
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_all_funciones(self):
            try:
                sql = 'SELECT funciones.idFuncion, peliculas.p_TituloPelicula, salas.noSala, funciones.f_fecha, funciones.f_Hora FROM funciones JOIN peliculas ON peliculas.idPelicula = funciones.f_idPelicula JOIN salas ON salas.noSala = funciones.f_noSala'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                print(err)
                return err

        def read_funiones_fecha(self, fecha):
            try:
                sql = 'SELECT funciones.idFuncion, peliculas.p_TituloPelicula, salas.noSala, funciones.f_fecha, funciones.f_Hora FROM funciones JOIN peliculas ON peliculas.idPelicula = funciones.f_idPelicula and funciones.f_fecha = %s JOIN salas ON salas.noSala = funciones.f_noSala'
                vals = (fecha,)                
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err

        def read_funciones_tituloPelicula(self, tituloPelicula):
            try:
                sql = 'SELECT funciones.idFuncion, peliculas.p_TituloPelicula, salas.noSala, funciones.f_fecha, funciones.f_Hora FROM funciones JOIN peliculas ON peliculas.idPelicula = funciones.f_idPelicula and peliculas.p_TituloPelicula = %s JOIN salas ON salas.noSala = funciones.f_noSala'
                vals = (tituloPelicula,)
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def update_funcion(self, fields, vals):
            try:
                sql = 'UPDATE funciones SET'+','.join(fields)+'WHERE idFuncion = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def delete_funcion(self, idFuncion):
            try:
                sql = 'DELETE FROM funciones WHERE idFuncion = %s'
                vals = (idFuncion,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def verifica_funcion(self, idPelicula, noSala, fecha, hora):
            try:
                sql = 'SELECT * FROM funciones WHERE f_idPelicula = %s and f_noSala = %s and f_fecha = %s and f_Hora = %s'
                vals = (idPelicula, noSala, fecha, hora)
                self.cursor.execute(sql, vals)
                return True
            except connector.Error as err:
                return err
        """
        *************** Metodos Asientos ***************
        """
        def create_asiento(self, noSala, noAsiento, estado):
            try:
                sql = 'INSERT INTO asientos (`asi_noSala`, `asi_NoAsiento`, `asi_estado`) VALUES (%s, %s, %s)'
                vals = (noSala, noAsiento, estado)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def read_a_asiento(self, idAsiento):
            try:
                #sql = 'SELECT asientos.*, salas.* FROM asientos JOIN salas ON salas.noSala = asientos.asi_noSala and asientos.idAsiento = %s'
                sql = 'SELECT asientos.idAsiento, salas.noSala, asientos.asi_NoAsiento, asientos.asi_estado FROM asientos JOIN salas ON salas.noSala = asientos.asi_noSala and asientos.idAsiento = %s'
                vals = (idAsiento,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err
        
        def read_all_asietos(self):
            try:
                sql = 'SELECT asientos.idAsiento, salas.noSala, asientos.asi_NoAsiento, asientos.asi_estado FROM asientos JOIN salas ON salas.noSala = asientos.asi_noSala'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err
        
        def read_no_asiento(self, noAsiento):
            try:
                sql = 'SELECT asientos.idAsiento, salas.noSala, asientos.asi_NoAsiento, asientos.asi_estado FROM asientos JOIN salas ON salas.noSala = asientos.asi_noSala and asientos.asi_NoAsiento = %s'
                vals = (noAsiento,)
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err

        def update_asiento(self, fields, vals):
            try:
                sql = 'UPDATE asientos SET'+','.join(fields)+'WHERE idAsiento = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        def delete_asiento(self, idAsiento):
            try:
                sql = 'DELETE FROM asietos WHERE idAsiento = %s'
                vals = (idAsiento,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err

        """
        *************** Metodos Boletos ***************
        """
        def create_boleto(self, idFuncion, idAsiento, idPelicula, noSala, precio):
            try:
                sql = 'INSERT INTO boletos (`b_idFuncion`, `b_idAsiento`, `b_idPelicula`, `b_noSala`, `b_Precio`) VALUES (%s, %s, %s, %s, %s)'
                vals = (idFuncion, idAsiento, idPelicula, noSala, precio)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err
        
        def read_a_boleto(self, idBoleto):
            try:
                sql = 'SELECT boletos.idBoleto, funciones.idFuncion, funciones.f_Hora, asientos.idAsiento, peliculas.p_TituloPelicula, salas.noSala, boletos.b_Precio FROM boletos JOIN funciones ON funciones.idFuncion = boletos.b_idFuncion JOIN asientos ON asientos.idAsiento = boletos.b_idAsiento JOIN peliculas ON peliculas.idPelicula = boletos.b_idPelicula JOIN salas ON salas.noSala = boletos.b_noSala and boletos.idBoleto = %s'
                vals = (idBoleto,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_all_boletos(self):
            try:
                sql = 'SELECT boletos.idBoleto, funciones.idFuncion, funciones.f_Hora, asientos.idAsiento, peliculas.p_TituloPelicula, salas.noSala, boletos.b_Precio FROM boletos JOIN funciones ON funciones.idFuncion = boletos.b_idFuncion JOIN asientos ON asientos.idAsiento = boletos.b_idAsiento JOIN peliculas ON peliculas.idPelicula = boletos.b_idPelicula JOIN salas ON salas.noSala = boletos.b_noSala'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                print(err)
                return err
        
        def update_boleto(self, fields, vals):
            try:
                sql = 'UPDATE boletos SET'+','.join(fields)+'WHERE idBoleto = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def delete_boleto(self, idBoleto):
            try:
                sql = 'DELETE FROM boletos WHERE idBoleto = %s'
                vals = (idBoleto,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err

        """
        *************** Metodos ticket ***************
        """
        def create_ticket(self, idUsuario, fecha, hora, Total):
            try:
                sql = 'INSERT INTO ticket (`t_idUsuario`, `t_Fecha`, `t_Hora`, `t_Total`) VALUES (%s, %s, %s, %s)'
                vals = (idUsuario, fecha, hora, Total)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                idTicket = self.cursor.lastrowid
                return idTicket
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err
        
        def read_a_ticket(self, idTicket):
            try:
                sql = 'SELECT ticket.idTicket, usuarios.u_Nombre, usuarios.u_APaterno, ticket.t_Fecha, ticket.t_Hora, ticket.t_Total FROM ticket JOIN usuarios ON usuarios.idUsuario = ticket.t_idUsuario and ticket.idTicket = %s'
                vals = (idTicket,)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                print(err)
                return err
        
        def read_all_ticket(self):
            try:
                sql = 'SELECT ticket.idTicket, usuarios.u_Nombre, usuarios.u_APaterno, ticket.t_Fecha, ticket.t_Hora, ticket.t_Total FROM ticket JOIN usuarios ON usuarios.idUsuario = ticket.t_idUsuario'
                self.cursor.execute(sql)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                print(err)
                return err
        
        def update_ticket(self, fields, vals):
            try:
                sql = 'UPDATE ticket SET'+','.join(fields)+'WHERE idTicket = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err

        def delete_ticket(self, idTicket):
            try:
                sql = 'DELETE FROM ticket WHERE idTicket = %s'
                vals = (idTicket,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        """
        *************** Metodos detalleVentaBoleto ***************
        """
        def create_detalleVentaBoleto(self, idBoleto, idTicket, cantidad, totalBoletos):
            try:
                sql = 'INSERT INTO detalleventaboleto (`dvb_idBoleto`,`dvb_idTicket`, `dvb_Cantidad`, `dvb_TotalBoletos`) VALUES (%s, %s, %s, %s)'
                vals = (idBoleto, idTicket, cantidad, totalBoletos)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                print(err)
                return err

        def read_a_detalleVentaBoleto(self, idBoleto, idTicket):
            try:
                sql = 'SELECT boletos.idBoleto, boletos.b_idFuncion, boletos.b_Precio, detalleventaboleto.dvb_Cantidad, detalleventaboleto.dvb_TotalBoletos FROM detalleventaboleto JOIN boletos ON boletos.idBoleto = detalleventaboleto.dvb_idBoleto and detalleventaboleto.dvb_idBoleto = %s and detalleventaboleto.dvb_idTicket = %s'
                vals = (idBoleto, idTicket)
                self.cursor.execute(sql, vals)
                record = self.cursor.fetchone()
                return record
            except connector.Error as err:
                return err

        def read_detalleVentaBoleto(self, idTicket):
            try:
                sql = 'SELECT boletos.idBoleto, boletos.b_idFuncion, boletos.b_Precio, detalleventaboleto.dvb_Cantidad, detalleventaboleto.dvb_TotalBoletos FROM detalleventaboleto JOIN boletos ON boletos.idBoleto = detalleventaboleto.dvb_idBoleto and detalleventaboleto.dvb_idTicket = %s'
                vals = (idTicket,)
                self.cursor.execute(sql, vals)
                records = self.cursor.fetchall()
                return records
            except connector.Error as err:
                return err

        def update_detalleVentaBoleto(self, fields, vals):
            try:
                sql = 'UPDATE detalleventaboleto SET'+','.join(fields)+'WHERE dvb_idBoleto = %s and dvb_ticket = %s'
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return err
        
        def delete_detalleVentaBoleto(self, idBoleto, idTicket):
            try:
                sql = 'DELETE FROM detalleventaboleto WHERE dvb_idBoleto = %s anddvb_idTicket = %s'
                vals = (idBoleto, idTicket)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                count = self.cursor.rowcount
                return count
            except connector.Error as err:
                self.cnx.rollback()
                return err