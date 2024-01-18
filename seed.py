from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.chat.model import Chat
from application.message.model import Message
from application.places.model import Place
from application.activities.model import Activity
from application.plans.model import Plan
from application.reviews.model import Review
from application.notification.model import Notification
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
                   username='janedoe123', email='jane.doe@gmail.com', images=[])
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

guide1 = Guide(place_id=1, name='Guy Dunn', tagline="Just a dude", user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com', info="Just a guy", availible_from=datetime.now(),availible_to=datetime.now(), images=["https://images.pexels.com/photos/775358/pexels-photo-775358.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"])

guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

chat1 = Chat(sender=2, receiver=1)
chat2 = Chat(sender=2, receiver=3)
chat3 = Chat(sender=2, receiver=4)
chat4 = Chat(sender=2, receiver=5)
db.session.add_all([chat1, chat2, chat3, chat4])
db.session.commit()

message1_1 = Message(chat_id=1, sender_id=2, text="Hey!", time="11:08")
message1_2 = Message(chat_id=1, sender_id=1, text="Hey!", time="11:08")
message1_3 = Message(chat_id=1, sender_id=2, text="How are you?", time="11:09")
message1_4 = Message(chat_id=1, sender_id=1, text="I'm great, and you?", time="11:11")
message1_5 = Message(chat_id=1, sender_id=2, text="Great! I love the look of your plan", time="11:12")

message2_1 = Message(chat_id=2, sender_id=2, text="Hey!", time="11:08")
message2_2 = Message(chat_id=2, sender_id=3, text="Hey, how are you?", time="11:08")

message3_1 = Message(chat_id=3, sender_id=2, text="Hey!", time="11:08")

message4_1 = Message(chat_id=4, sender_id=2, text="Hey!", time="11:08")
message4_2 = Message(chat_id=4, sender_id=2, text="Your plan looks great!", time="11:08")
db.session.add_all([message1_1, message1_2, message1_3, message1_4, message1_5, message2_1, message2_2, message3_1, message4_1, message4_2])
db.session.commit()

activity = Activity(name="canoe", location="nyc",
                    filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY", images=['https://i.cbc.ca/1.4764103.1532699684!/fileImage/httpImage/canoeing.jpg'])

db.session.add(activity)

guide1.activities.append(activity)
tourist1.guides.append(guide1)

# ... (existing code)


def create_tourist(name, user_type, username, email, images):
    tourist = Tourist(name=name, user_type=user_type,
                      username=username, email=email, images=images or [])
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


def create_review(guide_id, tourist_id, rating, title, comment=None):
    review = Review(
        guide_id=guide_id,
        tourist_id=tourist_id,
        rating=rating,
        title=title,
        comment=comment,
        timestamp=datetime.now()
    )
    db.session.add(review)
    # db.session.commit()
    # return review



def create_activity(name, location, filters, place_id, description, zip_code, images=None):
    activity = Activity(name=name, location=location, filters=filters,
                        place_id=place_id, description=description, zip_code=zip_code, images=images or [])

    db.session.add(activity)


def create_guide_activity_pairs(guide_data, activity_data):
    for guide_info in guide_data:
        guide = Guide.query.filter_by(username=guide_info[4]).first()
        guide_filters = set(guide_info[6])
        guide_place_id = guide_info[0]
        for activity_info in activity_data:
            activity_filters = set(activity_info[2])
            activity_place_id = activity_info[3]
            if guide_filters.intersection(activity_filters) and guide_place_id == activity_place_id:
                activity = Activity.query.filter_by(
                    name=activity_info[0]).first()
                guide.activities.append(activity)


# Add more tourists
tourist_data = [
    ('John Smith', 'TOURIST', 'johnsmith456', 'john.smith@gmail.com', ['https://images.pexels.com/photos/1043474/pexels-photo-1043474.jpeg']),
    ('Emily Wilson', 'TOURIST', 'emilywilson789', 'emily.wilson@gmail.com', ['https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1']),
    ('Michael Brown', 'TOURIST', 'michaelbrown123', 'michael.brown@gmail.com', []),
    ('Sophia Rodriguez', 'TOURIST', 'sophiarodriguez456', 'sophia.rodriguez@gmail.com', []),
    ('Daniel Taylor', 'TOURIST', 'danieltaylor789', 'daniel.taylor@gmail.com', []),
    ('Olivia Johnson', 'TOURIST', 'oliviajohnson234', 'olivia.johnson@gmail.com', []),
    ('Matthew Davis', 'TOURIST', 'matthewdavis567', 'matthew.davis@gmail.com', []),
    ('Isabella Martinez', 'TOURIST', 'isabellamartinez890', 'isabella.martinez@gmail.com', []),
    ('Ethan White', 'TOURIST', 'ethanwhite123', 'ethan.white@gmail.com', []),
    ('Ava Anderson', 'TOURIST', 'avaanderson456', 'ava.anderson@gmail.com', []),
    ('Noah Harris', 'TOURIST', 'noahharris789', 'noah.harris@gmail.com', []),
    ('Sophie Clark', 'TOURIST', 'sophieclark123', 'sophie.clark@gmail.com', []),
    ('William Turner', 'TOURIST', 'williamturner456', 'william.turner@gmail.com', []),
    ('Emma Lee', 'TOURIST', 'emmalee789', 'emma.lee@gmail.com', []),
    ('James Mitchell', 'TOURIST', 'jamesmitchell123', 'james.mitchell@gmail.com', []),
    ('Aria Thompson', 'TOURIST', 'ariathompson456', 'aria.thompson@gmail.com', []),
    ('Liam Garcia', 'TOURIST', 'liamgarcia789', 'liam.garcia@gmail.com', []),
    ('Grace Adams', 'TOURIST', 'graceadams123', 'grace.adams@gmail.com', []),
    ('Logan Moore', 'TOURIST', 'loganmoore456', 'logan.moore@gmail.com', []),
    ('Sophie Turner', 'TOURIST', 'sophieturner987', 'sophie.turner@gmail.com', []),
    ('Henry Miller', 'TOURIST', 'henrymiller234', 'henry.miller@gmail.com', []),
    ('Ella Parker', 'TOURIST', 'ellaparker567', 'ella.parker@gmail.com', []),
    ('Carter Brown', 'TOURIST', 'carterbrown890', 'carter.brown@gmail.com', []),
    ('Chloe Davis', 'TOURIST', 'chloedavis123', 'chloe.davis@gmail.com', []),
    ('Owen Smith', 'TOURIST', 'owensmith456', 'owen.smith@gmail.com', []),
    ('Madison Clark', 'TOURIST', 'madisonclark789', 'madison.clark@gmail.com', []),
    ('Jackson White', 'TOURIST', 'jacksonwhite123', 'jackson.white@gmail.com', []),
    ('Scarlett Taylor', 'TOURIST', 'scarletttaylor456', 'scarlett.taylor@gmail.com', []),
    ('Gabriel Hernandez', 'TOURIST','gabrielhernandez789', 'gabriel.hernandez@gmail.com', []),
    ('Zoe Adams', 'TOURIST', 'zoeadams123', 'zoe.adams@gmail.com', []),
    ('Nathan Wilson', 'TOURIST', 'nathanwilson456', 'nathan.wilson@gmail.com', []),
    ('Peyton Moore', 'TOURIST', 'peytonmoore789', 'peyton.moore@gmail.com', []),
    ('Hannah Martinez', 'TOURIST', 'hannahmartinez123', 'hannah.martinez@gmail.com', []),
    ('Landon Johnson', 'TOURIST', 'landonjohnson456', 'landon.johnson@gmail.com', []),
    ('Lily Harris', 'TOURIST', 'lilyharris789', 'lily.harris@gmail.com', []),
    ('Max Anderson', 'TOURIST', 'maxanderson123', 'max.anderson@gmail.com', []),
    ('Avery Turner', 'TOURIST', 'averyturner456', 'avery.turner@gmail.com', []),
    ('Evan Garcia', 'TOURIST', 'evangarcia789', 'evan.garcia@gmail.com', []),
    ('Mia Adams', 'TOURIST', 'miaadams123', 'mia.adams@gmail.com', []),
    ('Nicholas Baker', 'TOURIST', 'nicholasbaker234', 'nicholas.baker@gmail.com', []),
    ('Aubrey Cooper', 'TOURIST', 'aubreycooper567', 'aubrey.cooper@gmail.com', []),
    ('Zachary Turner', 'TOURIST', 'zacharyturner890', 'zachary.turner@gmail.com', []),
    ('Samantha Mitchell', 'TOURIST','samanthamitchell123', 'samantha.mitchell@gmail.com', []),
    ('Oscar Thompson', 'TOURIST', 'oscarthompson456', 'oscar.thompson@gmail.com', []),
    ('Aaliyah Wilson', 'TOURIST', 'aaliyahwilson789', 'aaliyah.wilson@gmail.com', []),
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
    (2, 'Hiroshi Tanaka', "Navigate Tokyo's Urban Jungle with Hiroshi – Your City Safari Guide!", 'GUIDE', 'hiroshi88', 'hiroshi.tanakaj@gmail.com', ['CULTURAL', 'SHOPPING', 'ENTERTAINMENT'], datetime.now(), one_year_from_now,
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
    (2, 'Haruki Ito', "Discover Tokyo's Green Oases with Haruki – Your Nature Explorer!", 'GUIDE', 'haruki123', 'haruki.ito@gmail.com', ['NATURE', 'OUTDOOR_ACTIVITIES', 'WELLNESS'], datetime.now(), one_year_from_now,
     "Nature enthusiast and entertainment aficionado, Haruki Ito, promises a guided experience that seamlessly combines the tranquility of nature with the excitement of entertainment hubs. Haruki's tours unfold against breathtaking natural backdrops, allowing visitors to connect with the environment. Dive into the thrill of entertainment, creating memories that resonate with both serenity and exhilaration."     ,[
        "https://images.pexels.com/photos/2584041/pexels-photo-2584041.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
        "https://images.pexels.com/photos/2480382/pexels-photo-2480382.jpeg",
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
    (2, 'Ryota Kobayashi', "Unlock Tokyo's Night Secrets with Ryota – Your Nightlife Navigator!", 'GUIDE', 'kobayashi789', 'ryota.kobayashi@gmail.com', ['CULTURAL', 'NIGHTLIFE', 'MUSIC', 'HOLIDAY_EVENTS', 'ENTERTAINMENT'], datetime.now(), one_year_from_now,
     "Cultural connoisseur and nightlife maven, Ryota Kobayashi, invites you on a guided exploration that reveals the city's cultural treasures by day and comes alive with the vibrant energy of nightlife. Ryota's tours are a dynamic fusion of cultural insights and the pulsating rhythm of the city after dark. Expect a well-rounded experience that captures the essence of the city's day and night offerings."     ,  [
        
        "https://images.pexels.com/photos/7803592/pexels-photo-7803592.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "https://images.pexels.com/photos/11289988/pexels-photo-11289988.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

])
]
for data in guide_data:
    create_guide(*data)

db.session.commit()

# for i in range(1, 11): 
#     for j in range(1, 7): 
#         notification = Notification(sender=i, receiver=j)
#         db.session.add(notification)

# db.session.commit()

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


create_guide_activity_pairs(guide_data, activity_data)
db.session.commit()


review_data = [
    (2, 1, 5, "Excellent Guide!", "Had an incredible experience with this guide! Their deep knowledge and passion for the subject made the tour absolutely fascinating. They went above and beyond to ensure everyone had a memorable time. I would highly recommend this guide to anyone looking for an enriching experience."),
    (2, 2, 4, "Informative but Room for Improvement", "The tour was very informative, and the guide did a great job covering a wide range of historical facts. However, I wished for a bit more interaction and engagement. Overall, a good experience, but there's room for improvement."),
    (2, 3, 3, "Average Experience", "Found the overall experience to be average. The guide's commentary lacked depth, and the tour could have been more engaging. It was an okay experience, but I expected more from the tour."),
    (2, 4, 5, "Fantastic Tour!", "This guide is fantastic! From start to finish, the tour exceeded all expectations. The guide's storytelling skills and attention to detail were impressive. Highly recommended for an outstanding tour experience."),
    (2, 5, 2, "Not Satisfied", "Unfortunately, I was not satisfied with the service provided by the guide. Their disinterest was evident, and it impacted the overall experience negatively. I expected a more enthusiastic and engaging tour."),
    (2, 6, 4, "Good, but Room for Improvement",
     "Had a good experience with this tour guide. They were knowledgeable and interacted well with the group. The tour was informative and enjoyable, but there's still room for improvement."),
    (2, 7, 3, "Could Be Better Organized", "The tour could have been better organized. Some aspects felt rushed, and there were moments of confusion. Despite this, the guide was friendly and tried to make the best of the situation."),
    (2, 8, 5, "Absolutely Fantastic!", "Absolutely fantastic experience! The guide was not only knowledgeable but also created a fun and memorable atmosphere. Every moment of the tour was enjoyable, and I would highly recommend it."),
    (2, 9, 1, "Terrible Service", "Terrible service from the guide. Their unprofessionalism and rudeness made the tour an unpleasant experience. I would advise against choosing this guide for any future tours."),

    (3, 10, 5, "Amazing Tour with Enthusiastic Guide",
     "An amazing tour with an exceptional guide! The guide's enthusiasm, coupled with breathtaking views, made this tour unforgettable. Highly recommended for anyone seeking a top-notch experience."),
    (3, 11, 4, "Enjoyed Every Moment", "Enjoyed every moment of the tour. The guide's pacing and storytelling were spot-on. A well-structured and entertaining experience, but there's always room for a bit more excitement."),
    (3, 12, 3, "Decent Guide but Room for Improvement",
     "Found the guide to be decent. The tour provided some information, but I expected a bit more depth and variety. It was an okay experience, but improvements could enhance the overall tour."),
    (3, 13, 5, "Outstanding Service!", "Outstanding service from the guide! Went above and beyond with insightful commentary and a well-planned itinerary. This tour exceeded all expectations, and I would gladly recommend it."),
    (3, 14, 2, "Not Worth the Money", "Regrettably, the tour was not worth the money. The content lacked interesting details, and the overall experience was underwhelming. Disappointed with the value provided."),
    (3, 15, 4, "Well-Planned and Enjoyable", "A well-planned tour that covered a variety of attractions. The guide's knowledge and engagement kept the tour interesting. Overall, a good experience with a few moments of brilliance."),
    (3, 16, 3, "Average Experience", "Found the overall experience to be average. The tour lacked the wow factor, and the guide's commentary could have been more engaging. An okay tour, but there's room for improvement."),
    (3, 17, 5, "Top-Notch Guide!", "This guide is top-notch! Their enthusiasm, coupled with in-depth knowledge, created a memorable tour experience. I would highly recommend this guide for an enriching and enjoyable tour."),
    (3, 18, 1, "Worst Tour Ever", "Worst tour ever. The guide was disorganized and unprepared, resulting in a regrettable experience. I would strongly advise against choosing this guide for any future tours."),

    (4, 19, 5, "Exceptional Guide with Humor", "Exceptional guide! Engaged the group with captivating storytelling and a great sense of humor. This guide made the tour both educational and entertaining. Highly recommended for an unforgettable experience."),
    (4, 20, 4, "Very Knowledgeable Guide", "The guide was very knowledgeable, providing a deep understanding of the subject matter. A well-structured and informative tour that I enjoyed. However, there's always room for improvement."),
    (4, 21, 3, "Room for Improvement", "The tour could improve in certain areas. Some parts felt lacking in variety, and the guide's interaction with the group could be enhanced. A decent tour with potential for enhancement."),
    (4, 22, 5, "Highly Recommended!", "Highly recommended! This tour exceeded all expectations. The guide's passion and attention to detail made it the best tour I've ever taken. An outstanding experience that I would gladly repeat."),
    (4, 23, 2, "Disappointed with the Tour",
     "Disappointed with the tour. The guide seemed uninterested, impacting the overall experience negatively. Expected a more engaging and enthusiastic tour."),
    (4, 24, 4, "Great Experience", "Had a great experience with this tour. It was well-organized and enjoyable. The guide's enthusiasm and knowledge kept the tour interesting. A memorable experience with a few exceptional moments."),
    (4, 25, 3, "Not Bad, Not Great", "The tour was not bad, but it wasn't great either. Average content and presentation. There's room for improvement to make the tour more engaging and memorable."),
    (4, 26, 5, "Fantastic Service!", "Fantastic service from the guide! Friendly, accommodating, and passionate about the tour. Every moment was enjoyable, and I would highly recommend this guide for an outstanding experience."),
    (4, 27, 1, "Awful Tour", "An awful tour with a disinterested guide. The lack of preparation and professionalism made it a regrettable experience. I would strongly advise against choosing this guide for any future tours."),

    (5, 28, 5, "Excellent Guide with Passion",
     "An excellent guide! Their knowledge and passion shone through, making the tour both educational and enjoyable. Highly recommended for a top-notch experience."),
    (5, 29, 4, "Informative and Enjoyable",
     "Informative tour that covered a wide range of topics. The guide's engaging commentary kept the group interested. A well-structured and enjoyable experience."),
    (5, 30, 3, "Average Experience", "Found the overall experience to be average. Expected a bit more excitement and variety. The guide's commentary could have been more engaging."),
    (5, 31, 5, "Highly Recommended for Professionalism",
     "Highly recommended! The guide was professional and engaging, creating a fantastic experience. Every moment was enjoyable, making it a tour worth repeating."),
    (5, 32, 2, "Not Satisfied with the Service",
     "Unfortunately, I was not satisfied with the service. The tour lacked excitement, and the guide's disinterest was evident. Expected a more engaging and enthusiastic experience."),
    (5, 33, 4, "Good Tour Guide", "Had a good experience with this tour guide. They were personable and knowledgeable, keeping the group engaged. The tour was enjoyable, with a few exceptional moments."),
    (5, 34, 3, "Room for Improvement", "The tour could be better. The guide should improve presentation skills to make the experience more engaging. Overall, an average tour with potential for improvement."),
    (5, 35, 5, "Fantastic Experience!", "A fantastic experience! Enjoyed every moment of the tour. The guide's enthusiasm and knowledge created a memorable atmosphere. Highly recommended for an outstanding tour."),
    (5, 36, 1, "Terrible Service", "Terrible service from the guide. Their rudeness and unhelpfulness made the tour an unpleasant experience. I would strongly advise against choosing this guide for any future tours."),

    (6, 37, 5, "Amazing Tour with Unique Insights",
     "An amazing tour with an exceptional guide! Captivating stories and unique insights made this tour unforgettable. Highly recommended for anyone seeking a top-notch experience."),
    (6, 38, 4, "Enjoyed Every Moment", "Enjoyed every moment of the tour. The guide's well-structured and informative commentary kept the group engaged. A memorable experience with a few moments of brilliance."),
    (6, 39, 3, "Decent Guide with Potential",
     "Found the guide to be decent. Expected more interaction with the group, but the tour provided some interesting information. An okay experience with room for improvement."),
    (6, 40, 5, "Outstanding Service!", "Outstanding service from the guide! Went above and beyond with insightful commentary and a well-planned itinerary. This tour exceeded all expectations, and I would gladly recommend it."),
    (6, 41, 2, "Not Worth the Money",
     "Regrettably, the tour was not worth the money. Lacked substance and interesting details. Disappointed with the overall value provided."),
    (6, 42, 4, "Well-Planned and Enjoyable", "A well-planned tour that covered a variety of interesting spots. The guide's knowledge and engagement kept the tour interesting. Overall, a good experience with a few moments of brilliance."),
    (6, 43, 3, "Average Experience", "Found the overall experience to be average. The tour could have been more engaging, and the guide's commentary lacked excitement. An okay tour with potential for improvement."),
    (6, 44, 5, "Top-Notch Guide!", "This guide is top-notch! Knowledgeable and personable, creating a memorable tour experience. Highly recommended for an enriching and enjoyable tour."),
    (6, 45, 1, "Worst Tour Ever", "Worst tour ever. The guide seemed unprepared and disinterested, resulting in a regrettable experience. I would strongly advise against choosing this guide for any future tours."),
]

for data in review_data:
    create_review(*data)

    db.session.commit()



def create_plan(tourist_id, guide_id, place_id, date_from, date_to, status, notes, activity_ids):
    plan = Plan(
        tourist_id=tourist_id,
        guide_id=guide_id,
        place_id=place_id,
        date_from=date_from,
        date_to=date_to,
        status=status,
        notes=notes
    )

    # Add activities to the plan
    for activity_id in activity_ids:
        activity = Activity.query.get(activity_id)
        if activity:
            plan.activities.append(activity)

    # Add the plan to the database
    db.session.add(plan)
    db.session.commit()


plan_data = [
    (1, 2, 2, "2022-02-17T12:30:00", "2022-01-17T12:30:00",
     "COMPLETED", "Let's go karaoke bar!", [1, 2, 3]),
    (2, 3, 3, "2022-01-01T12:30:00", "2021-12-30T12:30:00",
     "ONGOING", "Exploring historical sites", [4, 5, 6]),
    (3, 4, 4, "2021-12-15T12:30:00", "2021-12-10T12:30:00",
     "UPDATING", "Culinary adventure", [7, 8, 9]),
    (4, 5, 5, "2021-11-28T12:30:00", "2021-11-25T12:30:00",
     "UPDATING", "Nature exploration", [10]),
    (5, 6, 6, "2021-11-10T12:30:00", "2021-11-05T12:30:00",
     "CANCELLED", "Shopping spree", [1, 2, 3, 4]),
    (6, 2, 2, "2022-03-01T12:30:00", "2022-02-25T12:30:00",
     "UPDATING", "Art exploration", [5, 6, 7]),
    (7, 2, 2, "2022-02-15T12:30:00", "2022-02-10T12:30:00",
     "UPDATING", "Cultural immersion", [8, 9, 10]),
    (8, 2, 2, "2022-01-28T12:30:00", "2022-01-25T12:30:00",
     "BOOKED", "Nightlife experience", [1, 2, 3, 4]),
    (9, 2, 2, "2022-01-10T12:30:00", "2022-01-05T12:30:00",
     "CANCELLED", "Outdoor adventure", [6, 7, 8]),
    (10, 2, 2, "2021-12-25T12:30:00", "2021-12-20T12:30:00",
     "ONGOING", "Local festivities", [9, 10]),
]

for data in plan_data:
    create_plan(*data)

chat_data = [

]

