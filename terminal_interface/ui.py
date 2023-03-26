import os
from time import sleep

from domains.posts import Posts, PostInterface

class TerminalUI:
    def __init__(self):
        self.final_action = 0
        self.topic = 0
        self.tags = ''
        self.topic_page = 1

    # flows
    def init(self):
        self._clear_console()
        topic = self._get_topic()
        
        # handle invalid input
        if not self._is_valid_input(topic, self.TOPICS):
            self._send_invalid_message()
            sleep(2)
            return self.init()
        
        self._set_topic(topic)   
        # handle exit case
        if self.topic == 0:
            self._clear_console()
            return
                 
        self.init_tags_flow()

    def init_tags_flow(self):
        self._clear_console()
        tags = self._get_tags()
        self._set_tags(tags)
        self.init_response_flow()

    def init_response_flow(self):
        _, topic_actions, topic_interface = self.selected_topic
        
        actions = topic_actions(self.tags)
        json_response = actions.get()
        print(topic_interface.format_output(json_response))
        self.init_after_response_flow()

    def init_after_response_flow(self):
        final_action = self._get_final_action()
        
        # handle invalid input
        if not self._is_valid_input(final_action, self.FINAL_ACTIONS):
            self._send_invalid_message()
            return self.init_after_response_flow()
        
        self._set_final_action(final_action)   
        # handle exit case
        if self.final_action == 0:
            self._clear_console()
            return
        
        _, action_method, __ = self.selected_final_action
        action_method()
        
    # validations
    def _is_valid_input(self, topic, property):
        try:
            topic = int(topic)

            if topic == 0:
                return True
            
            for _topic in property:
                if topic in _topic:
                    return True
                
        except ValueError:
            return False
        
    # messages
    def _send_invalid_message(self):
        print('The inserted value is invalid, please try again...\n')

    def _clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    # props, sets, gets
    TOPICS = (
        (1, Posts, PostInterface()),
        # (2, 'Tags'),
    )

    @property
    def FINAL_ACTIONS(self):
        return (
            (1, self.init, 'More results'),
            (2, self.init_tags_flow, 'Search for different tags'),
            (3, self.init, 'Search for different topics')
        )
    
    @property
    def selected_topic(self):
        for topic in self.TOPICS:
            if self.topic in topic:
                return topic
            
    @property
    def selected_final_action(self):
        for final_action in self.FINAL_ACTIONS:
            if self.final_action in final_action:
                return final_action

    def _get_topic(self):
        topics = ''.join(
            [f'\n{index} - {interface.domain_name}' for index, _, interface in self.TOPICS]
        )
        return input(f'Select a topic:\n0 - Exit{topics}\n\n>')

    def _set_topic(self, topic):
        self.topic = int(topic)

    def _get_final_action(self):
        final_actions = ''.join(
            [f'\n{index} - {text}' for index, _, text in self.FINAL_ACTIONS]
        )
        return input(f'Select an action:\n0 - Exit{final_actions}\n\n>')

    def _set_final_action(self, final_action):
        self.final_action = int(final_action)

    def _set_topic_page(self, topic_page):
        self.topic_page = topic_page
        
    def _get_tags(self):
        _, __, topic_interface = self.selected_topic

        print(topic_interface.selection_message)
        return input(topic_interface.input_message).strip()

    def _set_tags(self, tags):
        self.tags = tags
        