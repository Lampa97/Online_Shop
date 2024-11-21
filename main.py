from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_get(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            with open("html/contacts.html", "r", encoding="utf-8") as file:
                page_content = file.read()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")
        else:
            self.send_response(200)
            self.send_header("Content-type",
                             "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_content, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")