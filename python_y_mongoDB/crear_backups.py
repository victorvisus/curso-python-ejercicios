from bson import json_util


def backup_a_json(_db_name, _col_name, _client):
    collection = _client[_db_name][_col_name]
    data = list(collection.find())

    with open(f"./ficheros/{_db_name}_{_col_name}.json", "w") as f:
        f.write(json_util.dumps(data, indent=4))

    print("✅ Archivo JSON generado.")
