from fastapi import FastAPI, HTTPException, Query, Depends
from lab.config import settings
from lab.database import connect_to_database
from lab.models import User


class App:
    def __init__(self):

        self.app = FastAPI()

        # Регистрируем маршруты
        self.app.add_api_route("/nodes", self.get_all_nodes, methods=["GET"])
        self.app.add_api_route("/nodes/{node_id}", self.get_node_and_relations, methods=["GET"])
        self.app.add_api_route("/nodes", self.create_nodes_and_relations, methods=["POST"])
        self.app.add_api_route("/nodes/{node_id}", self.delete_node_and_relations, methods=["DELETE"])

    def authenticate(self, api_key: str = Query(...)):
        if api_key != settings.API_SECRET_KEY:
            raise HTTPException(status_code=401, detail="Unauthorized")

    def get_all_nodes(self):
        self.db = connect_to_database()
        query = """
            MATCH (n:User)
            RETURN n AS node
            LIMIT 50
            """
        results, _ = self.db.cypher_query(query)
        nodes = [
            {"element_id": row[0].element_id, "properties": dict(row[0].items())}
            for row in results
        ]
        return {"nodes": nodes}

    def get_node_and_relations(self, node_id: int):
        self.db = connect_to_database()
        query = """
            MATCH (n {id: $node_id})-[r]->(m)
            RETURN n AS node, r AS relation, m AS related_node
            """
        results, _ = self.db.cypher_query(query, {"node_id": node_id})

        nodes_and_relations = []
        for row in results:
            nodes_and_relations.append({
                "node": {
                    "id": row[0].id,
                    "labels": list(row[0].labels),
                    "properties": dict(row[0].items())
                },
                "relation": {
                    "type": row[1].type,
                    "properties": dict(row[1].items())
                },
                "related_node": {
                    "id": row[2].id,
                    "labels": list(row[2].labels),
                    "properties": dict(row[2].items())
                }
            })

        return {"node_and_relations": nodes_and_relations}

    def create_nodes_and_relations(self, data: dict, api_key: str = Depends(authenticate)):
        self.db = connect_to_database()
        try:
            nodes = []
            for user_data in data['nodes']:
                node = User(user_id=user_data['user_id'], screen_name=user_data['screen_name'],
                            full_name=user_data['full_name']).save()
                nodes.append(node)

            for rel in data.get('relations', []):
                related_node = User.nodes.get(user_id=rel['related_node_id'])
                for node in nodes:
                    node.following.connect(related_node)

            return {"message": "Nodes and relations created successfully", "nodes": [node.user_id for node in nodes]}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete_node_and_relations(self, node_id: str, api_key: str = Depends(authenticate)):
        self.db = connect_to_database()
        try:
            nodes = User.nodes.filter(user_id=node_id).all()

            if not nodes:
                raise HTTPException(status_code=404, detail=f"Node with user_id {node_id} not found")

            for node in nodes:
                for rel in node.following:
                    node.following.disconnect(rel)

                node.delete()

            return {"message": f"Nodes with user_id {node_id} and their relations have been deleted"}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


app_instance = App()
app = app_instance.app
