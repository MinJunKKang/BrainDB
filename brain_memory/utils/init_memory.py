import os
import redis
import mysql.connector

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FOLDERS = [
    os.path.join(BASE_DIR, "data"),
    os.path.join(BASE_DIR, "gui"),
    os.path.join(BASE_DIR, "utils")
]

def create_folders():
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        print(f"Folder created or exists: {folder}")

# 로컬 Redis 연결 (기본 포트 6379, DB 0)
def init_redis():
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        print("Redis connection successful.")
    except Exception as e:
        print("Redis connection failed:", e)

# 로컬 MySQL 연결 (사용자명과 비밀번호를 환경에 맞게 변경)
def init_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kang4652@"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS memory_db")
        print("MySQL connection successful. Database 'memory_db' is ready.")
        cursor.close()
        conn.close()
    except Exception as e:
        print("MySQL connection failed:", e)

def init_project():
    print("Initializing project...")
    create_folders()
    init_redis()
    init_mysql()