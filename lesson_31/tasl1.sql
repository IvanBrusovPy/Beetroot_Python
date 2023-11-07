CREATE TABLE test_table(
  test_field INT
);
ALTER TABLE test_table RENAME TO test_table_2_0

INSERT INTO test_table_2_0(test_field)
VALUES (1)

UPDATE test_table_2_0
SET new_field = ("Hello")
WHERE test_field = 1

DELETE FROM test_table_2_0 WHERE test_field = 1