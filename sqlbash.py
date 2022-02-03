import sqlite3
import os
import typer

app = typer.Typer()

@app.command()
def main(file:str=None):
    if file:
        fname,fext = os.path.splitext(file)
        db = sqlite3.connect(fname+".db")
        sql = open(file).read()
        cur = db.cursor()
        for statement in sql.split(";"):
            cur.execute(statement)
            print(cur.fetchall())
            db.commit()

    else:
        db = sqlite3.connect(":memory:")
        while True:
            cmd = input("sqlite3> ")
            if cmd.startswith("connect"):
                try:
                    com, conn = cmd.split(" ")
                    db = sqlite3.connect(conn)
                except Exception as error:
                    print(error)
            elif cmd == "sql":
                cur = db.cursor()
                cur.execute(input("> "))
                print(cur.fetchall())
            elif cmd == "commit":
                db.commit()
            elif cmd == "exit":
                break;
app()
