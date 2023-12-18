from flask import Flask,render_template,jsonify
app = Flask(__name__)
# print(app)

JOBS = [
  {
    "id" : 1,
    "title" : "Python Developer",
    "location" : "Banglore,India",
    "salary" : "Rs.15,00,000"
  },
  {
    "id" : 2,
    "title" : "Java Developer",
    "location" : "Delhi,India",
    "salary" : "Rs.10,00,000"
  },
  {
    "id" : 3,
    "title" : "Data Analyst",
    "location" : "New York",
    "salary" : "$50,000,000"
  },
  {
    "id" : 4,
    "title" : "Frontend Developer",
    "location" : "Remote",
    "salary" : "Rs.50,00,000"
  }
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name="MyProject")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)