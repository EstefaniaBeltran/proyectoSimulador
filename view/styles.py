def style_app():
    return """
    QWidget {
        background-color: #9a8678;
        font-family: 'Georgia';
        color: #3b2f2f;
    }

    QWidget#Banner {
        background-color: black;
    }

    QLabel.title {
        font-size: 70px;
        color: white;
        font-family: 'Georgia';
    }

    QLabel.subtitle {
        font-size: 30px;
        color: white;
    }

    QGroupBox {
        background-color: #c6b5a5;
        border: 3px solid #7a6a5a;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    QPushButton {
        background-color: #e0d2c3;
        padding: 8px;
        border: 2px solid #7a6a5a;
        border-radius: 6px;
        font-size: 14px;
        width:50px;
    }

    QPushButton:hover {
        background-color: #f0e6dd;
    }

    QLineEdit {
        background-color: #e9dfd8;
        border: 2px solid #7a6a5a;
        border-radius: 6px;
        padding: 4px;
        font-size: 14px;
    }
    """