import sqlite3
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.con=sqlite3.connect('student.db')
    def create(self):
        
        cur_obj=self.con.cursor()
        cur_obj.execute("create table if not exists student (id integer, name text)")
        
    def query(self):
        cur_obj=self.con.cursor()
        str=f"insert into student(id,name) values ({self.id},'{self.name}')"
        cur_obj.execute(str)
        self.con.commit()
        cur_obj.execute("Select * from student")
        data=cur_obj.fetchall()
        return data
        