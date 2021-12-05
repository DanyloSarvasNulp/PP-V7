from DataBase.debug_enable import app
import DataBase.Blueprint.userRequests, DataBase.Blueprint.auditoriumRequests, DataBase.Blueprint.accessRequests


if __name__ == "__main__":
    app.run(debug=True)
