class Facebook:
    def __init__(self, facebookId):  # Class constructor
        self.facebookId = facebookId
        self.idUrls = []
        self.noIdUrls = ['https://facebook.com/search/%s/photos-of',
                         'https://facebook.com/search/%s/photos-tagged',
                         'https://facebook.com/search/%s/photos-commented',
                         'https://facebook.com/search/%s/photos-liked',
                         'https://facebook.com/search/%s/stories',
                         'https://facebook.com/search/%s/stories-commented',
                         'https://facebook.com/search/%s/stories-liked',
                         'https://facebook.com/search/%s/videos-tagged',
                         'https://facebook.com/search/%s/videos-commented',
                         'https://facebook.com/search/%s/videos-liked',
                         'https://facebook.com/search/%s/groups']
        self.description = ['Check blocked photos',
                            'Check tagged phtos',
                            'Commented photos',
                            'Liked photos',
                            'Posts',
                            'Commented posts',
                            'Liked posts',
                            'Tagged videos',
                            'Commented videos',
                            'Liked videos',
                            'Joined groups']
    
    # function to insert "facebookId" on "idUrls"
    def insert_id(self):
        for url in self.noIdUrls:
            self.idUrls.append(url % (self.facebookId))  # Append url+id on the "idUrls" list
        # returns the final url
        self.result()
    
    # function to print the result
    def result(self):
        print('###############################################')
        for x in range(len(self.description)):
            print(self.description[x])
            print('<a>' + self.idUrls[x] + '</a>')
            print('')
        print('###############################################')
