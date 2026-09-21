from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Change Image</title>
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
                max-height: 400px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 20px 0;
            }
            button {
                padding: 10px 24px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
                background: #3498db;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background: #2980b9;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <img id="myImage" src="https://picsum.photos/id/237/600/400" alt="Random image">
        <button onclick="changeImage()">Change Image</button>

        <script>
            function changeImage() {
                var img = document.getElementById("myImage");
                // Uses picsum.photos and a random number to fetch a new image each click
                var randomId = Math.floor(Math.random() * 1000);
                img.src = "https://picsum.photos/600/400?random=" + randomId;
            }
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
