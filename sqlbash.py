import sqlite3

def connect(db):
    return sqlite3.connect(db)

def exec(db,*,code):
    cur = db.cursor()
    cur.execute(code)
    db.commit()

def mainloop(__prompt):
    print("PySQL-Bash 1.9.2")
    print("Creator: DS_Stift007 (https://github.com/Stift007/sqlbash)")
    db = connect(input("Enter Database Name: "))
    while True:
        print(__prompt)
        cmd = input("$ ")
        if cmd=="RET":
            break
        else:
            exec(db=db,code=cmd)

if __name__ == "__main__":
        mainloop("sql@sql-bash.localhost:5000")