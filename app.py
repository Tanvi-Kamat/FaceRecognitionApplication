import flask
from flask import request, render_template
import face_recognizer

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# shows the home page to upload photo file with submit button
@app.route('/')
def home():
    return render_template('index.html')

# when redirected to uploadedimage page,
@app.route('/uploadedimage', methods=['GET', 'POST'])
def uploadedimage():
    if request.method == "POST":
        # object with file's information
        upimage = request.files['file']
        # saving image's path and name
        upimage.save('/Users/tanvikamat/images/' + upimage.filename)
        # store image name (a string)
        image_file = '/Users/tanvikamat/images/' + upimage.filename
        # Call the function inside face_recognizer.py to return the JSON data
        # store user's image points from app.py
        json_data = face_recognizer.get_encodings(image_file)
        # return the file that will be displayed and what the result will be (json_data)
        return render_template('uploadedimage.html', result=json_data)
        # (return)display output data (successfully uploaded image)

app.run()
