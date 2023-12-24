from sqlalchemy import create_engine, text
import os
connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM  jobs"))
    print("type(result):",type(result))
    jobs = []
    # Fetch all results
    result_all = result.fetchall()

    # Accessing column names
    column_names = result.keys()

    for row in result_all:
      jobs.append(dict(zip(column_names,row)))

    return jobs

  