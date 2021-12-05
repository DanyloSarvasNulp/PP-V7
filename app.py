from DataBase.config_app import app, db
import DataBase.Blueprint.userRequests, DataBase.Blueprint.auditoriumRequests, DataBase.Blueprint.accessRequests


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
