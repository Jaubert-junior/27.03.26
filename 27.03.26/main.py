from flask import Flask, render_template
from routes import indexRouter

app = Flask(__name__)

indexRouter.adicionarRotas(app=app)

app.run(debug = True)