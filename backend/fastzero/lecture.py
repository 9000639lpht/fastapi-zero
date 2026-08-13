from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/lecture', response_class=HTMLResponse)
def lecture_request():
    return """
    <html>
        <head>
            <title>Nosso ola mundo!</title>
        </head>
        <body>
            <h1>Ola Mundo</h1>
        </body>
     </html>"""
