from app import app
import Blueprint.userRequests, Blueprint.auditoriumRequests, Blueprint.accessRequests


if __name__ == "__main__":
    app.run(debug=True)
