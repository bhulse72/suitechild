from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/project.html')
def project():
    return render_template('./project.html')

@app.route('/ERDiagram.html')
def er_diagram():
    return render_template('./ERDiagram.html')

if __name__ == '__main__':
    app.run(debug=True)