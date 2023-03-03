from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'titel': 'Data Analyst',
  'location': 'Frankfurt am Main',
  'salary': '68.000 Euro',
}, {
  'id': 2,
  'titel': 'Data Scientist',
  'location': 'Hamburg',
  'salary': '80.000 Euro',
}, {
  'id': 3,
  'titel': 'Frontend Developer',
  'location': 'Remote'
}, {
  'id': 4,
  'titel': 'Senior Backend Developer',
  'location': 'Frankfurt am Main',
  'salary': '78.000 Euro',
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="NasTech")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
