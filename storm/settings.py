from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

db_name = env.str("DB_NAME")
db_user = env.str("DB_USER")
db_password = env.str("DB_PASSWORD")
db_server = env.str("DB_SERVER")
db_port = env.str("DB_PORT")

destination_types = ["email", "sms", "push", "whatsapp"]
