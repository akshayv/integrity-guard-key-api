from flask import Flask
from flask import Response
import pymysql
import re
import json

app = Flask(__name__)
@app.route("/keys/<domain>")
def get_keys(domain):
        conn = pymysql.connect(
                db='integrity_guard',
                user='root',
                passwd='6ae55bf9bee47738e977dcf7b3966a7d910575c5cf5fb76e',
                host='localhost')
        c = conn.cursor()
        c.execute("SELECT domain_regex, public_key FROM client_keys")
        for row in c.fetchall():
                if re.compile(row[0]).match(domain):
                        return Response(row[1], status=200)

        return Response("", status=200)



if __name__ == "__main__":
    app.run()
