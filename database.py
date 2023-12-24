from sqlalchemy import create_engine, text
import os
engine = create_engine(os.environ['DB_CONNECTION_STRING'])

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

  