from notion_client import Client
from pprint import pprint
import json

import Format_Message
import send_Message

notion_token = 'secret_WjqGmvQEH30VkR5YVe3Ug2rqN9rt8VSjwA6imPcAGyo'
notion_page_id = "5ca75bab843b4449a25974ffe7b29c96"
notion_database_id = "772566dcd28540e59884610806eea096"
justin_database_id = "b1f43304872747008fe2cd3325fdb967"



def write_text(client, page_id, text, type='paragraph'):
    client.blocks.children.append(
        block_id=page_id,
        children=[{
            "object": "block",
            "type": type,
            type: {
                "rich_text": [{"type": "text", "text": {"content": text}}]
            }
        }]
    )


def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content, indent=1)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)


def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def safe_get(data, dot_chained_keys):
    '''
        {'a': {'b': [{'c': 1}]}}
        safe_get(data, 'a.b.0.c') -> 1
    '''
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data


def create_simple_blocks_from_content(client, content):
    page_simple_blocks = []

    for block in content:

        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type].get('plain_text')



        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text'] if rich_text else ""  # Use an empty string if rich_text is empty
        }

        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_from_content(client, nested_children)

        page_simple_blocks.append(simple_block)

    return page_simple_blocks

def main(database):
    client = Client(auth=notion_token)

    # content = read_text(client, notion_page_id)
    #
    # write_dict_to_file_as_json(content, 'content.json')
    #
    # simple_blocks = create_simple_blocks_from_content(client, content)
    #
    # write_dict_to_file_as_json(simple_blocks, 'simple_blocks.json')


    db_info = client.databases.retrieve(database_id=database)

    write_dict_to_file_as_json(db_info, 'db_info.json')

    db_rows = client.databases.query(database_id=database)

    write_dict_to_file_as_json(db_rows, 'db_rows.json')

    simple_rows = []

    for row in db_rows['results']:
        Pre_Assignment = safe_get(row, 'properties.Assignment.title')
        Class = safe_get(row, 'properties.Class.select.name')
        Due_Date = safe_get(row, 'properties.Due Date.date.start')
        Status = safe_get(row, 'properties.Status.checkbox')

        Pre_Assignment = str(Pre_Assignment)
        Pre_Assignment = Pre_Assignment[39:]
        end_Index = (Pre_Assignment.find("'"))
        if end_Index == -1:
            continue
        Assignment = Pre_Assignment[0:end_Index]

        simple_rows.append({
            'Assignment': Assignment,
            'Class': Class,
            'Due_Date': Due_Date,
            'Status' : Status

        })

        write_dict_to_file_as_json(simple_rows, 'simple_rows.json')






databases = [notion_database_id, justin_database_id]

if __name__ == '__main__':
    for x in range(len(databases)):
        main(databases[x])
        message = Format_Message.get_Assignments(x)
        send_Message.send(message,x)