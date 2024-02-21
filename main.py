from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv
import pandas


app = Flask(__name__)
Bootstrap(app)
app.secret_key ="aishadarvesh"



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location=StringField('Cafe Location on google map', validators=[DataRequired(),URL()])
    opening=StringField("Opening time",validators=[DataRequired()])
    close=StringField("Closing time",validators=[DataRequired()])
    coffee=SelectField("Coffee Rating",validators=[DataRequired()],choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi = SelectField("Wifi Rating", validators=[DataRequired()],choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power = SelectField("Power Rating", validators=[DataRequired()],choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')



@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv",newline='',encoding="utf8",mode="a") as csv_file:
             csv_file.write(f"\n{form.cafe.data},"
                        f"{form.location.data},"
                        f"{form.opening.data},"
                        f"{form.close.data},"
                        f"{form.coffee.data},"
                        f"{form.wifi.data},"
                        f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafe')
def cafes():
     with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)
     return render_template('coffee.html',data=csv_data,cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
