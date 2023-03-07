create table if not exists clientes(
    id serial primary key not null,
    nome varchar(50) not null,
    nascimento date not null,
    credito float check(credito>=0.00) default 0.00,
    senha varchar(30) not null,
    email varchar(50) not null unique
);

create table if not exists jogos(
    id serial primary key not null,
    nome varchar(50) not null,
    publicadora varchar(50) not null,
    maior18 boolean not null,
    genero varchar(50) not null,
    preco float check(preco>=0.00) not null default 0.00

);

create table if not exists compra(
    id serial primary key not null,
    idCliente smallint NULL REFERENCES clientes (id),
    idJogo smallint NULL REFERENCES jogos (id),
	datacompra date not null default current_date
);



