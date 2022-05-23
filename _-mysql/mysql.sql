sa-- SQL used for to create atestatDB

CREATE TABLE users (
  id int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  username varchar(255) NOT NULL UNIQUE,
  password varchar(255) NOT NULL,
  created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL DEFAULT NULL
) ENGINE = atestatDB DEFAULT CHARSET=latin1;