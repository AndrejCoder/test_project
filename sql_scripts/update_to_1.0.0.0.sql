BEGIN;
  CREATE TABLE version_dbversion
  (
      id INT NOT NULL,
      version INT NOT NULL
  );
  insert into version_dbversion values (1, '1.0.0.0');
  update version_dbversion set version = '1.0.0.0' where id = 1;

  CREATE TABLE reports_report
  (
      id SERIAL PRIMARY KEY NOT NULL,
      name VARCHAR(255) NOT NULL,
      slug VARCHAR(100) NOT NULL,
      date DATE NOT NULL
  );

COMMIT;