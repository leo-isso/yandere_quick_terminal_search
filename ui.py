from posts import Posts

class TerminalUI:
    TOPICS = (
        (1, Posts),
        # (2, 'Tags'),
    )

    def __init__(self):
        self.exit_ui = False
        self.topic = 0

    def init(self,):
        while not self.exit_ui:
            topic = input('(1) images\n(2)tags\n(0)tags\nSearch for: ')

            try:
                self.topic = int(topic)
                if not self._is_valid_topic():
                    raise ValueError
            except ValueError:
                print('The inputed value is invalid')
                print('Exiting...')
                self.exit_ui = True
                continue
            


    def _is_valid_topic(self):
        if self.topic == 0:
            return False
        
        for topic in self.TOPICS:
            if self.topic in topic:
                return True
            
        return False