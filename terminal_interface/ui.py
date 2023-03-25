from domains.posts import Posts, PostInterface

class TerminalUI:
    TOPICS = (
        (1, Posts, PostInterface()),
        # (2, 'Tags'),
    )

    def __init__(self):
        self.exit_ui = False
        self.topic = 0

    def init(self,):
        topic = self._get_topic()

        if not self._is_valid_topic(topic):
            self._send_invalid_message()
            return self.init()
        
        self._set_topic(topic)            
        self.init_topic_flow()

    def init_topic_flow(self):
        _, topic_actions, topic_interface = self.selected_topic

        print(topic_interface.selected_message)
        tags = input(topic_interface.input_message)
        actions = topic_actions(tags)
        print(actions.get())
        
        self.exit_ui = True
        

    def _is_valid_topic(self, topic):
        try:
            topic = int(topic)

            if topic == 0:
                return True
            
            for _topic in self.TOPICS:
                if topic in _topic:
                    return True
                
        except ValueError:
            return False
        
    # messages
    def _send_invalid_message():
        print('\nThe inserted value is invalid, please try again...\n')


    # props, sets, gets
    @property
    def selected_topic(self):
        for topic in self.TOPICS:
            if self.topic in topic:
                return topic

    def _get_topic(self):
        topics = ''.join(
            [f'\n{index} - {interface.domain_name}' for index, _, interface in self.TOPICS]
        )
        return input(f'Select a topic:\n0 - Exit{topics}\n>')

    def _set_topic(self, topic):
        self.topic = int(topic)
        