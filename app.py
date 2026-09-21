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
                font-family: Arial, sans-serif;

                /* Garden gnome themed background: mossy green base
                   with soft radial "toadstool" and "hat" blobs */
                background-color: #2f5233;
                background-image:
                    radial-gradient(circle at 15% 20%, rgba(198, 40, 40, 0.55) 0, rgba(198, 40, 40, 0.55) 60px, transparent 61px),
                    radial-gradient(circle at 15% 20%, rgba(255, 255, 255, 0.9) 61px, rgba(255,255,255,0.9) 78px, transparent 79px),
                    radial-gradient(circle at 85% 75%, rgba(198, 40, 40, 0.55) 0, rgba(198, 40, 40, 0.55) 50px, transparent 51px),
                    radial-gradient(circle at 85% 75%, rgba(255, 255, 255, 0.9) 51px, rgba(255,255,255,0.9) 65px, transparent 66px),
                    radial-gradient(circle at 90% 15%, rgba(139, 195, 74, 0.35) 0, transparent 70px),
                    radial-gradient(circle at 10% 85%, rgba(139, 195, 74, 0.35) 0, transparent 90px),
                    linear-gradient(180deg, #3c6e47 0%, #2f5233 60%, #1f3d24 100%);
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            h1 {
                color: #fff8e1;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
            }
            .card {
                background: rgba(255, 248, 230, 0.92);
                padding: 30px 40px;
                border-radius: 16px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.35);
                text-align: center;
            }
            img {
                max-width: 90%;
                max-height: 400px;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 20px 0;
                border: 4px solid #c62828;
            }
            button {
                padding: 10px 24px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
                background: #c62828;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background: #a31f1f;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1 style="color:#3c6e47; text-shadow:none;">🍄 Hello, World! 🍄</h1>
            <img id="myImage" src="https://picsum.photos/id/237/600/400" alt="Random image">
            <br>
            <button onclick="changeImage()">Change Image</button>
        </div>

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
