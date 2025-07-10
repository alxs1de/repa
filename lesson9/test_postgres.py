from sqlalchemy import create_engine, inspect

db_connection_string = "postgresql://postgres:123@localhost:5432/postgresbb"
db = create_engine(db_connection_string)

# 0 = users
# 1 = subject
# 2 = student
# 3 = group_student
# 4 = teacher

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'subject'

def test_add_subject():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (201, 'Chinese')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 201")
    assert result.rowcount == 1
    connect.execute("delete from subject where subject_id = 201")

def test_edit_subject():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (201, 'Chinese')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 201")
    assert result.rowcount == 1
    connect.execute("UPDATE subject SET subject_title = 'Portuguese' WHERE subject_id = 201")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 201").fetchall()
    assert result[0][1] == 'Portuguese'
    connect.execute("delete from subject where subject_id = 201")

def test_delete_subject():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (202, 'Chinese')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 202")
    assert result.rowcount == 1
    connect.execute("delete from subject where subject_id = 202")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 202")
    assert result.rowcount == 0

