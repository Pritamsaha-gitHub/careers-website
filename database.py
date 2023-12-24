from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://uv5wbcgkuwpk3n8e:2KQn4jiDNCcdJo3m9fxt@bb6wpf6bmuizq5veeckw-mysql.services.clever-cloud.com/bb6wpf6bmuizq5veeckw?charset=utf8mb4")

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

  