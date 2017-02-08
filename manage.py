import os, sys
import dbconfig

def create():
    from sqlalchemy import Table
    import model
    for (name, table) in vars(model).iteritems():
        if isinstance(table, Table):
            table.create()

def run():
    import urls
    if os.environ.get("REQUEST_METHOD", ""):
        from wsgiref.handlers import BaseCGIHandler
        BaseCGIHandler(sys.stdin, sys.stdout, sys.stderr, os.environ).run(urls.urls)
    else:
        from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
        httpd = WSGIServer(('', 8080), WSGIRequestHandler)
        httpd.set_app(urls.urls)
        print "Serving HTTP on %s port %s ..." % httpd.socket.getsockname()
        httpd.serve_forever()

if __name__=="__main__":
    if 'create' in sys.argv:
        create()

    if 'run' in sys.argv:
        run()

    #print("All Tables in the DB:")
    #for t in dbconfig.metadata.sorted_tables:
    #    print(t.name)
    #print("Tables end.")

    result = dbconfig.connection.execute("select title from entry")
    for row in result:
        print("title: ", row['title'])
