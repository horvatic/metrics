class HttpResponse:
    def __init__(self, handler) -> None:
        self.handler = handler

    def set_status_code(self, status_code):
        self.handler.send_response(status_code)

    def set_content_type(self, header):
        self.handler.send_header("Content-type", header)
        self.handler.end_headers()

    def set_status_content(self, content):
        self.handler.wfile.write(bytes(content, "utf-8"))
