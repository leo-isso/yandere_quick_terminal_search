class PostInterface:
    domain_name = 'Images'
    selection_message = 'Images selected'
    input_message = 'Search for tags: '

    def format_output(self, json_response):
        if not len(json_response) > 0:
            return '\nSorry, no results found\n'

        output = ''

        for item in json_response:
            id = item['id']
            file_url = item['file_url']
            tags = item['tags']

            output = f'{output}\nID: {id}\nFile URL: {file_url}\nTags: {tags}\n'

        return output
