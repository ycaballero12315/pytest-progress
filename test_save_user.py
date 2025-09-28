from db_other import save_user

def test_save_user(mocker):
    mock_connect = mocker.patch('db_other.sqlite3.connect')
    
    # El objeto conexión que devuelve connect()
    mock_conn = mock_connect.return_value 
    mock_cursor = mock_conn.cursor.return_value

    save_user('Yoe', 41)

    mock_connect.assert_called_once_with('/data/users.db')
    
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users(name, age) VALUES (?, ?)", ("Yoe", 41)
    )

    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()  