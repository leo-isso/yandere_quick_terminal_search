from posts import Posts 

if __name__ == '__main__':
    tags_input = input('Type the tags you\'re looking for: ')
    posts = Posts(tags=tags_input)
    print(posts.get())