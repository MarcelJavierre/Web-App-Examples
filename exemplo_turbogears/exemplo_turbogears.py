from tg import expose, TGController

# Abre o arquivo com o documento HTML, lê todo o conteúdo e fecha o arquivo
indexFile = open("./html/index.html", "r", encoding="UTF-8")
indexContent = indexFile.read()
indexFile.close()

class RootController(TGController):
    @expose()
    def index(self):
        return indexContent

from tg import MinimalApplicationConfigurator

config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController()
})

application = config.make_wsgi_app()

from wsgiref.simple_server import make_server

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()
