class TagsInterface:
    domain_name = 'Tags'
    selection_message = 'Tags selected'
    input_message = 'Search for tags: '

    def format_output(self, json_response):
        if not len(json_response) > 0:
            return '\nSorry, no results found\n'

        output = ''

        for item in json_response:
            id_ = item['id']
            name = item['name']
            count = item['count']

            output = f'{output}\nID: {id_}\nTag name: {name}\nResults: {count}\n'

        return output
