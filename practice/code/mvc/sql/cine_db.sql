create database if not exists cine_db;
use cine_db;

create table if not exists administradores(
	idAdministrador int not null auto_increment,
    a_Usuario varchar(30) not null,
    a_Contrasena varchar(30) not null,
    a_Nombre varchar(50) not null,
    a_APaterno varchar(50) not null,
    a_AMaterno varchar(50),
    a_Correo varchar(100) not null,
    primary key(idAdministrador)
)engine = InnoDB;

create table if not exists usuarios(
	idUsuario int not null auto_increment,
    u_Nombre varchar(50) not null,
    u_APaterno varchar(50) not null,
    u_AMaterno varchar(50),
    u_Correo varchar(100),
    primary key(idUsuario)
)engine = InnoDB;

create table if not exists peliculas(
	idPelicula int not null auto_increment,
    p_TituloPelicula varchar(50) not null,
    p_Clasificacion varchar(5) not null,
    p_Genero varchar(20) not null,
    p_Duracion varchar(10) not null,
    primary key(idPelicula)
)engine = InnoDB;

create table if not exists salas(
	noSala int not null auto_increment,
    s_NoPasillos int not null,
    s_NoAsientos int not null,
    primary key(noSala)
)engine = InnoDB;

create table if not exists funciones(
	idFuncion int not null auto_increment,
    f_idPelicula int,
    f_noSala int,
    f_fecha date not null,
    f_Hora varchar(10) not null,
    primary key(idFuncion),
    constraint fk_peliculas_funciones foreign key(f_idPelicula)
		references peliculas(idPelicula) 
        on delete cascade
        on update cascade,
	constraint fk_salas_funciones foreign key(f_noSala)
		references salas(noSala)
        on delete cascade
        on update cascade
)engine = InnoDB;

create table if not exists asientos(
	idAsiento int not null auto_increment,
    asi_noSala int,
    asi_NoAsiento int not null,
    asi_estado enum('ocupado', 'libre') not null,
    primary key(idAsiento),
    constraint fk_salas_asientos foreign key(asi_noSala)
		references salas(noSala)
        on delete cascade
        on update cascade
)engine = InnoDB;

create table if not exists boletos(
	idBoleto int not null auto_increment,
    b_idFuncion int,
    b_idAsiento int,
    b_idPelicula int,
    b_noSala int,
    b_Precio float not null,
    primary key(idBoleto),
    constraint fk_funciones_boletos foreign key(b_idFuncion)
		references funciones(idFuncion)
        on delete cascade
        on update cascade,
	constraint fk_asientos_boletos foreign key(b_idAsiento)
		references asientos(idAsiento)
        on delete cascade
        on update cascade,
	constraint fk_peliculas_boletos foreign key(b_idPelicula)
		references peliculas(idPelicula)
        on delete cascade
        on update cascade,
	constraint fk_salas_boletos foreign key(b_noSala)
		references salas(noSala)
        on delete cascade
        on update cascade
)engine = InnoDB;

create table if not exists ticket(
	idTicket int not null auto_increment,
    t_idUsuario int,
    t_Fecha date not null,
    t_Hora time not null,
    t_Total float not null,
    primary key(idTicket),
	constraint fk_usuarios_ticket foreign key(t_idUsuario)
		references usuarios(idUsuario)
        on delete cascade
        on update cascade
)engine = InnoDB;

create table if not exists detalleVentaBoleto(
	dvb_idBoleto int not null,
    dvb_idTicket int not null,
    dvb_Cantidad int not null,
    dvb_TotalBoletos float not null,
    primary key(dvb_idBoleto, dvb_idTicket),
    constraint fk_boletos_detalleVentaBoleto foreign key(dvb_idBoleto)
		references boletos(idBoleto)
        on delete cascade
        on update cascade,
	constraint  fk_ticket_detalleVentaBoleto foreign key(dvb_idTicket)
		references ticket(idTicket)
        on delete cascade
        on update cascade
)engine = InnoDB;