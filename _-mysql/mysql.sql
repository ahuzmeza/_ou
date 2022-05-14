-- SQL used for to create atestatDB

CREATE DATABASE MyNoteDb;

CREATE TABLE users (
  id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  username varchar(255) NOT NULL UNIQUE,
  password varchar(255) NOT NULL,
  created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL DEFAULT NULL
) ENGINE = MyNoteDb DEFAULT CHARSET=latin1;

CREATE TABLE user_notes (
  id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  username_id varchar(255) NOT NULL,
  note_body text NOT NULL,
  created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL DEFAULT NULL
);
