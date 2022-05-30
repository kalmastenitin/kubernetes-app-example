from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
import time
import pathlib
import mysql.connector


def create_database():
    global db_created
    attempts = 150

    while attempts > 0:
        attempts -= 1
        time.sleep(2)
        try:
            mydb = mysql.connector.connect(
                host="mysql-service",
                user="root",
                password="secretpassword",
            )
            if mydb.is_connected():
                # console_logger.debug("db_conected successfully")
                mycursor = mydb.cursor()
                mycursor.execute("SHOW DATABASES")
                dbExist = False
                db_created = False
                for x in mycursor:
                    if x[0] == "test":
                        dbExist = True
                if not dbExist:
                    print("creating new db")
                    db_created = True
                    mycursor.execute(f"CREATE DATABASE test")
                mycursor.execute("SHOW DATABASES")
                for x in mycursor:
                    if x[0] == "test":
                        dbExist = True
                return dbExist
            return False
        except Exception as e:
            print("retrying db connection ...")
    return


def create_static():
    static_server = pathlib.PurePath.joinpath(
        pathlib.Path.cwd().parent, "workspace", "static")
    pathlib.Path.mkdir(static_server, mode=777, exist_ok=True)
    return static_server


def create_app():
    app = FastAPI(
        title="Vredefort Backend",
        description="Contains User Registration and Authorization with Project Management",
        version="3.0.0",
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/v1/docs"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    from .project_manager.routes import router as service_router
    app.include_router(
        service_router, prefix="/api/v1/pm")
    from .auth.routes import router as auth_router
    app.include_router(
        auth_router, prefix="/api/v1/auth")
    return app


db = create_database()

static_dir = create_static()
app = create_app()
