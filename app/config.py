SECRET_KEY = 'e341e6698cb20dd889d040a9be7d5fc129cb06255f349bd6ea3f901afe8d61b4'
# ip='postgres_db'
ip = 'localhost'
PGUSER='postgres'
PGPASSWORD='linky1337'
DATABASE='taxi_project'
PORT=5432

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}:{PORT}/{DATABASE}'