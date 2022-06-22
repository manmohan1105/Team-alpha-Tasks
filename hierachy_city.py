"""
Write a python code to show the hierarchy of different cities provided in json file. Hierarchy is based on two conditions:

1. City having parent_id null is the root city.

2. Every city is having a parent_id which is the id of another city. So, latter city will be parent of former city.

For Example:
{"name": "California","id": 99,"parent_id": null}
{"name": "Bay Area","id": 1, "parent_id": 99}
Here, parent_id of Bay Area is the id of California. So, California is the parent city of Bay Area and its hierarchy can be show as:

California
Bay Area

# input json format location file
location_txt = """
[{"name": "California","id": 99,"parent_id": null},{"name": "Bay Area","id": 1, "parent_id": 99},{"name":"Oakland","id": 2,"parent_id": 1},{"name": "Apple","id": 3,"parent_id": 6},{"name": "San Francisco","id": 6,"parent_id": 8},{"name": "San Francisco County","id": 8,"parent_id": 1},{"name": "New York City","id":4,"parent_id": null},{"name": "Brooklyn","id": 9,"parent_id": 4},{"name": "Manhattan","id": 5,"parent_id": 4}, { "name": "Goldman Sachs","id": 10,"parent_id": 5}, { "name": "JPMorgan Chase","id": 11,"parent_id": 5}]
"""

# output
California
-Bay Area
--Oakland
--San Francisco County
--San Francisco
--Apple
--New York City
--Brooklyn
--Manhattan
--Goldman Sachs
--JPMorgan Chase
"""





from collections import defaultdict
def function(arr):
    
    def dfs(node,visited):
        order_list.append(id_to_name[node])
        visited.add(node)
        for child_node in parent_mapping[node]:
            if child_node not in visited:
                dfs(child_node,visited)


    id_to_name = defaultdict(str)
    parent_mapping = defaultdict(list)
    start_nodes = []
    for entry in arr:
        id_to_name[entry["id"]] = entry["name"]
        if entry["parent_id"] != "":
          parent_mapping[entry["parent_id"]].append(entry["id"])
        else:
            start_nodes.append(entry["id"])
    order_list=[]
    visited=set()
    for node in start_nodes:
        dfs(node,visited)
    print(order_list)
function([{"name": "California","id": 99,"parent_id": ""},{"name": "Bay Area","id": 1, "parent_id": 99},{"name":"Oakland","id": 2,"parent_id": 1},{"name": "Apple","id": 3,"parent_id": 6},{"name": "San Francisco","id": 6,"parent_id": 8},{"name": "San Francisco County","id": 8,"parent_id": 1},{"name": "New York City","id":4,"parent_id": ""},{"name": "Brooklyn","id": 9,"parent_id": 4},{"name": "Manhattan","id": 5,"parent_id": 4}, { "name": "Goldman Sachs","id": 10,"parent_id": 5}, { "name": "JPMorgan Chase","id": 11,"parent_id": 5}])    
