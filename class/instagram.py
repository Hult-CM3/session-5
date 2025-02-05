class User:
    def __init__(self, username, bio):
        self.username = username
        self.bio = bio
        self.followers = 0
        self.posts = []

    def follow(self, another_user):
        another_user.followers += 1
        print(f"{self.username} followed {another_user.username}!")

    def add_post(self, post):
        self.posts.append(post)
        print(f"{self.username} added a new post: {post.caption}")
class Post:
    def __init__(self, image, caption):
        self.image = image
        self.caption = caption
        self.likes = 0

    def like(self):
        self.likes += 1
        print(f"Post '{self.caption}' now has {self.likes} likes!")
class Reel:
    def __init__(self, video, caption, music):
        self.video = video
        self.caption = caption
        self.music = music
        self.views = 0

    def play(self):
        self.views += 1
        print(f"Reel '{self.caption}' played! Total views: {self.views}")
# Creating users
alice = User("alice123", "Traveler & Photographer")
bob = User("bob_reacts", "Tech reviews & memes")

# Following each other
alice.follow(bob)  
bob.follow(alice)  

# Alice creates a post
post1 = Post("beach_sunset.jpg", "Sunset at Bali!")
alice.add_post(post1)

# Bob likes Alice’s post
post1.like()

# Bob creates a reel
reel1 = Reel("unboxing.mp4", "New iPhone unboxing!", "Cool Tech Beats")
bob.add_post(reel1)

# Alice watches Bob's reel
reel1.play()
