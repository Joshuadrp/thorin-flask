import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    return render_template('about.html', page_title='About', company=data)


@app.route('/about/<member_name>')
def about_member(member_name):
    member = None

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        
        # Find the member with the matching `url`
        for obj in data:
            if obj["url"] == member_name:
                member = obj
                break  # Break the loop once the member is found

    # Handle the case where the member is not found
    if member is None:
        return abort(404, description="Member not found")
    
    # Return the member's name as an HTML response
    return render_template('member.html', member=member)



@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact')


@app.route('/careers')
def careers():
    return render_template('careers.html', page_title='Careers')

if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True #never set this to true in production, just in development environment, or when submitting a project.
    )