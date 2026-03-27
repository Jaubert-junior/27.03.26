from flask import Flask, render_template

def home():
    return render_template('index.html')
