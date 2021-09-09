class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def singasong(self):
        for line in self.lyrics:
            print(line)
s = Song(['''May God Bless You,
                    May God Bless You
                    Happy Birthday to You'''])
s.singasong()