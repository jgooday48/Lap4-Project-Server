from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity
from application.plans.model import Plan
from sqlalchemy import text
from datetime import datetime, timedelta

app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
tourist1 = Tourist(name='Jane Doe', user_type='TOURIST',
                   username='janedoe123', email='jane.doe@gmail.com')
tourist1.set_password('password')

db.session.add(tourist1)
db.session.commit()

name = "NYC"
tags = ["#photo"]
description = "The city that never sleeps"
location = "USA"
images = ["https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg"]

place = Place(name=name, tags=tags, description=description,
              location=location, images=images)
db.session.add(place)

one_year_from_now = datetime.now() + timedelta(days=365)

guide1 = Guide(place_id=1, name='Guy Dunn', tagline="Just a dude", user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com', info="Just a guy", availible_from=datetime.now(),availible_to=datetime.now())

guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc",
                    filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY", images=['sdsds'])

db.session.add(activity)

guide1.activities.append(activity)

# ... (existing code)


def create_tourist(name, user_type, username, email):
    tourist = Tourist(name=name, user_type=user_type,
                      username=username, email=email)
    tourist.set_password('password')
    db.session.add(tourist)


def create_place(name, tags, description, location, images=None):
    place = Place(name=name, tags=tags,
                  description=description, location=location, images=images or [])
    db.session.add(place)


def create_guide(place_id, name, tagline,  user_type, username, email, filters, availible_from, availible_to, info,  images=None):
    guide = Guide(place_id=place_id, name=name, tagline=tagline, user_type=user_type, username=username, email=email, availible_from=availible_from, availible_to=availible_to, info=info, images=images or [])
    guide.set_password('password')
    guide.filters = filters
    db.session.add(guide)



def create_activity(name, location, filters, place_id, description, zip_code, images=None):
    activity = Activity(name=name, location=location, filters=filters,
                        place_id=place_id, description=description, zip_code=zip_code, images=images or [])

    db.session.add(activity)


# Add more tourists
tourist_data = [
    ('John Smith', 'TOURIST', 'johnsmith456', 'john.smith@gmail.com'),
    ('Emily Wilson', 'TOURIST', 'emilywilson789', 'emily.wilson@gmail.com'),
    ('Michael Brown', 'TOURIST', 'michaelbrown123', 'michael.brown@gmail.com'),
    ('Sophia Rodriguez', 'TOURIST', 'sophiarodriguez456', 'sophia.rodriguez@gmail.com'),
    ('Daniel Taylor', 'TOURIST', 'danieltaylor789', 'daniel.taylor@gmail.com')
]

for data in tourist_data:
    create_tourist(*data)

db.session.commit()


# Add more places
place_data = [
    ("Tokyo", ["#technology"], "Futuristic city", "Japan",  [
     "https://media.cntraveller.com/photos/64f6f03779eae8fd6b04756b/16:9/w_1920,c_limit/japan-GettyImages-1345059895.jpeg"]),
    ("Malta", ["#beach"], "best island", "Europe"),
    ("Paris", ["#culture"], "City of Love", "France"),
    ("Sydney", ["#beach"], "Beautiful beaches", "Australia"),
    ("Rome", ["#history"], "Eternal City", "Italy"),
    ("Los Angeles", ["#city"], "vibrant city", "USA")
]

for data in place_data:
    create_place(*data)

db.session.commit()

# Add more guides
guide_data = [
    (2, 'Hiroshi Tanaka', "Navigate Tokyo's Urban Jungle with Hiroshi – Your City Safari Guide!", 'GUIDE', 'hiroshi88', 'hiroshi.tanakaj@gmail.com', ['CULTURAL', 'SHOPPING'], datetime.now(), one_year_from_now,
     "Meet Hiroshi, a seasoned guide with a deep appreciation for cultural nuances and a knack for uncovering hidden shopping gems. Hiroshi's passion lies in revealing the heart of the city, intertwining cultural narratives with the thrill of unique shopping experiences. His tours go beyond the ordinary, promising a journey filled with captivating stories, local insights, and an immersive exploration of the city's rich tapestry.",
     [
        "https://images.pexels.com/photos/5506098/pexels-photo-5506098.jpeg",
        "https://images.pexels.com/photos/5506143/pexels-photo-5506143.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    ] ),
    (2, 'Yuki Nakamura', "Savor Tokyo's Flavor Palette with Yuki – Your Culinary Companion!", 'GUIDE', 'yuki42', 'yuki.nakamura@gmail.com', ['HISTORICAL', 'FOOD', 'CULTURAL', 'FAMILY_FRIENDLY'], datetime.now(), one_year_from_now,
     "Yuki is a guide who bridges the gap between history and gastronomy, crafting experiences that resonate with both the intellect and the palate. Yuki's tours delve into the historical tapestry of the city, bringing stories to life, and exploring culinary treasures along the way. Expect a blend of historical significance and culinary delights, making Yuki's tours a satisfying and enriching adventure."     ,[
        "https://images.pexels.com/photos/8329668/pexels-photo-8329668.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/8329631/pexels-photo-8329631.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/8329300/pexels-photo-8329300.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        
        ]),
    (2, 'Haruki Ito', "Discover Tokyo's Green Oases with Kenji – Your Nature Explorer!", 'GUIDE', 'haruki123', 'haruki.ito@gmail.com', ['NATURE', 'ENTERTAINMENT', 'OUTDOOR_ACTIVITIES', 'WELLNESS'], datetime.now(), one_year_from_now,
     "Nature enthusiast and entertainment aficionado, Haruki Ito, promises a guided experience that seamlessly combines the tranquility of nature with the excitement of entertainment hubs. Haruki's tours unfold against breathtaking natural backdrops, allowing visitors to connect with the environment. Dive into the thrill of entertainment, creating memories that resonate with both serenity and exhilaration."     ,[
        "https://images.pexels.com/photos/2584041/pexels-photo-2584041.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
        "https://images.pexels.com/photos/2480382/pexels-photo-2480382.jpeg"
        "https://images.pexels.com/photos/2480379/pexels-photo-2480379.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    ]),
    (2, 'Kaori Fujimoto', "Find Zen in Tokyo's Hustle with Koari – Your Wellness Wanderlust Partner!", 'GUIDE', 'fujimoto456', 'koari.fujimoto@gmail.com', ['ART', 'OUTDOOR_ACTIVITIES', 'FEMALE_FRIENDLY'], datetime.now(), one_year_from_now,
     "Kaori Fujimoto, a versatile guide, crafts experiences that cater to art enthusiasts, outdoor adventurers, and those seeking a female-friendly environment. Kaori's tours are a celebration of artistic expression and the great outdoors, providing a welcoming space for all travelers. Immerse yourself in a journey that transcends traditional boundaries, blending art, nature, and inclusivity."     ,   [
        "https://images.pexels.com/photos/9783910/pexels-photo-9783910.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        "https://images.pexels.com/photos/9784751/pexels-photo-9784751.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/9784747/pexels-photo-9784747.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/9784035/pexels-photo-9784035.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/9784025/pexels-photo-9784025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
     ]),
    (2, 'Ryota Kobayashi', "Unlock Tokyo's Night Secrets with Ryota – Your Nightlife Navigator!", 'GUIDE', 'kobayashi789', 'ryota.kobayashi@gmail.com', ['CULTURAL', 'NIGHTLIFE', 'MUSIC', 'HOLIDAY_EVENTS'], datetime.now(), one_year_from_now,
     "Cultural connoisseur and nightlife maven, Ryota Kobayashi, invites you on a guided exploration that reveals the city's cultural treasures by day and comes alive with the vibrant energy of nightlife. Ryota's tours are a dynamic fusion of cultural insights and the pulsating rhythm of the city after dark. Expect a well-rounded experience that captures the essence of the city's day and night offerings."     ,  [
        
        "https://images.pexels.com/photos/7803592/pexels-photo-7803592.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/11289988/pexels-photo-11289988.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

])
]
for data in guide_data:
    create_guide(*data)

db.session.commit()

# Add more activities
activity_data = [
    ("hiking", "Tokyo", ["OUTDOOR_ACTIVITIES"], 2, "amazing views", "90210", [
        "https://cdn.cheapoguides.com/wp-content/uploads/sites/2/2017/08/Mt.-Kawanori.jpg"
    ]),
    ("museum tour", "Paris", ["CULTURAL", "HISTORICAL"],
     4, "art and history exploration", "75001", []),
    ("sushi cooking class", "Tokyo", ["FOOD", "CULTURAL"], 2, "learn the art of sushi making", "100-0005", [
        "https://images.wowcher.co.uk/images/deal/28955882/777x520/1151816.jpg"
    ]),
    ("beach volleyball", "Sydney", [
     "OUTDOOR_ACTIVITIES", "SPORTS"], 5, "fun in the sun", "2000", [
         "https://beachvolleyball.com.au/wp-content/uploads/2021/12/beach-play2.jpg"
     ]),
    ("Colosseum tour", "Rome", ["HISTORICAL","CULTURAL"], 6, "ancient wonders", "00184", [
        "https://colosseumrometickets.com/wp-content/uploads/2018/06/Woman-tourist-enjoying-the-view-of-the-Roman-Colosseum-in-Rome-Italy.jpg"
    ]),
    ("sakura viewing", "Tokyo", ["OUTDOOR_ACTIVITIES", "NATURE"], 2, "enjoy cherry blossoms", "111-0032", [
        "https://i1.wp.com/rakuten.today/wp-content/uploads/2023/03/sakura_feature_1500-1.png?w=1500&ssl=1"
    ]),
    ("live jazz performance", "Tokyo", ["MUSIC", "ENTERTAINMENT", "ART"], 2, "experience live jazz music", "106-0047", [
        "https://www.tokyoweekender.com/wp-content/uploads/2019/03/Sometime-Jazz-Club-Tokyo-Weekender-bw-1024x768.png"
    ]),
    ("disability-friendly art exhibition", "Tokyo", ["ART", "DISABILITY_FRIENDLY"], 2, "inclusive art showcase", "163-8001", [
        "https://d7hftxdivxxvm.cloudfront.net/?quality=80&resize_to=width&src=https%3A%2F%2Fartsy-media-uploads.s3.amazonaws.com%2F3DLWA9x_hysKzt3Umq4VtQ%252F3.jpg&width=1820"
    ]),
    ("traditional tea ceremony", "Tokyo", ["CULTURAL", "EDUCATIONAL"], 2, "learn the art of tea", "104-0061", [
        "https://static.nationalgeographic.co.uk/files/styles/image_3200/public/rstea2.webp?w=1450&h=816"
    ]),
    ("yoga in the park", "Tokyo", ["FITNESS", "OUTDOOR_ACTIVITIES", "WELLNESS"], 2, "relaxing outdoor yoga", "150-0001", [
        "https://www.travelandleisure.com/thmb/uydlfUJu7ccmFRGy2fm-BTSJSkA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/TAL-four-seasons-scottsdale-meditation-DESERTBATHE0823-9fef6def4e294df296fc2d2cb2aafa10.jpg"
    ]),
    ("family-friendly amusement park", "Tokyo", ["FAMILY_FRIENDLY", "ENTERTAINMENT"], 2, "fun for all ages", "135-0064", [
        "https://www.japan-guide.com/g18/6918_01.jpg"
    ]),
    ("adventure escape room", "Tokyo", ["ADVENTURE", "WORKSHOPS"], 2, "exciting puzzle challenges", "100-0014", [
        "https://blog.japanwondertravel.com/wp-content/uploads/2022/12/9train_playimage_1-1200x799.webp"
    ]),
    ("holiday lights festival", "Tokyo", ["HOLIDAY_EVENTS", "NIGHTLIFE"], 2, "festive light displays", "160-0023", [
        "https://media.timeout.com/images/105831159/1024/768/image.webp"
    ]),
    ("literary book club", "Tokyo", ["LITERATURE", "EDUCATIONAL", "ART"], 2, "discuss great books", "102-0093", [
        "https://www.myboutiquehotel.com/photos/101822/book-and-bed-tokyo-ikebukuro-tokyo-045-56456-1110x700.jpg"
    ]),
    ("arcade tournament", "Tokyo", ["GAMING", "ENTERTAINMENT", "ART"], 2, "competitive gaming fun", "163-8001", [
        "http://gaming.moe/wp/wp-content/uploads/2016/01/IMG_0237-1024x768.jpg"
    ]),
    ("photography workshop", "Tokyo", ["PHOTOGRAPHY", "WORKSHOPS"], 2, "capture stunning shots", "106-0047", [
        "https://i0.wp.com/japanorama.co.uk/wp-content/uploads/2016/10/shibuya_DSC0546a-1400px.jpg?w=1400&ssl=1"
    ]),
    ("wellness retreat", "Tokyo", ["WELLNESS", "FITNESS"], 2, "relax and rejuvenate", "150-0043", [
        "https://i0.wp.com/blueriseretreats.com/wp-content/uploads/2020/07/masaaki-komori-qwPSnBvdhtI-unsplash-1.jpg?fit=600%2C600&ssl=1"
    ]),
    ("street food festival", "Tokyo", ["FOOD", "ENTERTAINMENT"], 2, "savor delicious street food", "160-0023", [
        "https://images.squarespace-cdn.com/content/v1/59dc3ac1cd0f68a1402fce69/1569052371472-J11WGZAPKH8IE5VXN9Z8/koenji_DSC5776.jpg?format=1500w"
    ]),
    ("nightclub dance party", "Tokyo", ["NIGHTLIFE", "ENTERTAINMENT"], 2, "dance the night away", "160-0023", [
        "https://media.timeout.com/images/105766128/1024/768/image.webp"
    ]),
    ("women's empowerment workshop", "Tokyo", ["EDUCATIONAL", "FEMALE_FRIENDLY"], 2, "inspiring and informative", "100-0005", [
        "https://www.japantimes.co.jp/uploads/imported_images/uploads/2019/07/n-women-a-20190724.jpg"
    ]),
    ("female artists exhibition", "Tokyo", ["ART", "CULTURAL", "FEMALE_FRIENDLY"], 2, "celebrating women in art", "163-8001", [
        "https://6mirai.tokyo-midtown.com/interview/images/int121_main_02.jpg"
    ]),
    ("women in technology conference", "Tokyo", ["TECHNOLOGY", "EDUCATIONAL", "FEMALE_FRIENDLY"], 2, "empowering discussions", "100-0014", [
        "https://media.wired.com/photos/5955b87ecbd9b77a41915a2a/master/w_1920,c_limit/anitaborg_48913230.jpg"
    ]),
    ("dance fitness class", "Tokyo", ["FITNESS", "FEMALE_FRIENDLY"], 2, "fun workout for everyone", "106-0047", [
        "https://media.timeout.com/images/102638958/1024/576/image.webp"
    ]),
    ("yoga and self-care retreat", "Tokyo", ["WELLNESS", "FEMALE_FRIENDLY", "OUTDOOR_ACTIVITIES", "FITNESS"], 2, "focus on self-love", "150-0043", [
        "https://www.japantimes.co.jp/wp-content/uploads/2013/11/p3-yoga-a-20131128.jpg"
    ]),

]

for data in activity_data:
    create_activity(*data)




db.session.commit()
