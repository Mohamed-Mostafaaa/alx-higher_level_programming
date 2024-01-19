-- Script that creates a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states ( -- Query to create states table with 2 constraints
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
