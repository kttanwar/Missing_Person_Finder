from flask import Flask , render_template, request
import views
import dataSetCreator
import detector
import trainner
app = Flask(__name__)

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/index', 'index', views.index)
app.add_url_rule('/services', 'services', views.services)
app.add_url_rule('/ngo', 'ngo', views.ngo)
app.add_url_rule('/result', 'result', views.result)
app.add_url_rule('/services/upload', 'upload', views.upload)
app.add_url_rule('/services/search', 'search', views.search)

@app.route('/exec', methods=['GET','POST'])
def parse(name=None):
    if request.method == "POST":
        #get form data
        name = request.form.get('name')
        age = request.form.get('age')
        gen = request.form.get('gender')
        # location = request.form.get('location')
    
    dataSetCreator.test(name, age, gen) 
    
    trainner.test()
    return render_template('services.html',name=name)
@app.route('/exec2')
def parse2(name=None):
    
    detector.test() 
    return render_template('services.html',name=name)
if __name__ == "__main__":
    app.run(debug=True)