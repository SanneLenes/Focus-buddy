from flask import Flask, request
import os

app = Flask(__name__)

# Simpele "database"
taken = {
    "lezen": 0,
    "oefenen": 0,
    "mail": 0
}

@app.route("/")
def home():
    return """
    <h1>Welkom bij je Focus App</h1>
    <p>Scan je NFC tag om een taak te starten.</p>
    """

@app.route("/start")
def start_taak():
    taak = request.args.get('taak')

    if taak in taken:
        taken[taak] += 10
        return f"""
            <h1>Taak '{taak}' gestart!</h1>
            <p>Je hebt nu {taken[taak]} punten voor deze taak.</p>
            <a href="/">Terug naar home</a>
        """
    else:
        return "<h1>Onbekende taak.</h1><a href='/'>Terug</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
