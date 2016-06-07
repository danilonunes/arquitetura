drop table if exists contatos;
create table contatos (
  id integer primary key autoincrement,
  nome text not null,
  apelido text null,
  sexo  text not null,
  dt_nascimento date null
);

drop table if exists tipos_endereco;
create table tipos_endereco (
  id integer primary key autoincrement,
  nome text not null
);

drop table if exists enderecos_contato;
create table enderecos_contato (
  id_con integer primary key autoincrement,
  nome text not null
);
