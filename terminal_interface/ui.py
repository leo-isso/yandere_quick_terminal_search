from domain.posts import Posts, PostInterface

class TerminalUI:
    TOPICS = (
        (1, Posts, PostInterface),
        # (2, 'Tags'),
    )

    def __init__(self):
        self.exit_ui = False
        self.topic = 0

    def init(self,):
        while not self.exit_ui:
            topic = input('(1)images\n(2)tags\n(0)tags\nSearch for: ')

            try:
                self.topic = int(topic)
                if not self._is_valid_topic():
                    raise ValueError
            except ValueError:
                print('The inputed value is invalid')
                print('Exiting...')
                self.exit_ui = True
                continue
            
            self.init_topic_flow()
            
    def init_topic_flow(self):
        _, topic_actions, topic_interface = self._get_selected_topic()

        print(topic_interface.selected_message)
        tags = input(topic_interface.input_message)
        actions = topic_actions(tags)
        print(actions.get())
        
        self.exit_ui = True
        
    def _get_selected_topic(self):
        for topic in self.TOPICS:
            if self.topic in topic:
                return topic

    def _is_valid_topic(self):
        if self.topic == 0:
            return False
        
        for topic in self.TOPICS:
            if self.topic in topic:
                return True
            
        return False