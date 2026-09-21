from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello World</title>
        <style>
            body {
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                background: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #34495e;
            }
            img {
                max-width: 90%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <img src="/static/hello.png" alt="Hello World image">
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
