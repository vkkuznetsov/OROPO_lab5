from lab.main import App


def test_get_all_nodes():
    app_instance = App()

    response = app_instance.get_all_nodes()

    assert isinstance(response, dict)

    assert "nodes" in response
    assert isinstance(response["nodes"], list)


def test_get_node_and_relations():
    app_instance = App()

    response = app_instance.get_node_and_relations(1)

    assert isinstance(response, dict)

    assert "node_and_relations" in response
    assert isinstance(response["node_and_relations"], list)


def test_create_nodes_and_relations():
    app_instance = App()

    data = {
        "nodes": [
            {"user_id": 1, "screen_name": "user1", "full_name": "User One"},
            {"user_id": 2, "screen_name": "user2", "full_name": "User Two"}
        ],
        "relations": [
            {"related_node_id": 2}
        ]
    }

    response = app_instance.create_nodes_and_relations(data)

    assert isinstance(response, dict)

    assert "message" in response
    assert response["message"] == "Nodes and relations created successfully"


def test_delete_node_and_relations():
    app_instance = App()

    response = app_instance.delete_node_and_relations("1")

    assert isinstance(response, dict)

    assert "message" in response
    assert response["message"] == "Nodes with user_id 1 and their relations have been deleted"


def test_delete_node_and_relations2():
    app_instance = App()

    response = app_instance.delete_node_and_relations("2")

    assert isinstance(response, dict)

    assert "message" in response
    assert response["message"] == "Nodes with user_id 2 and their relations have been deleted"
