CREATE SEQUENCE example START WITH 1000 INCREMENT BY 3;

CREATE TABLE gov_employee(
    id INT GENERATED ALWAYS AS IDENTITY,
    gov_id INT DEFAULT nextval('example'),
    name TEXT,
    PRIMARY KEY(id)
);






-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;
