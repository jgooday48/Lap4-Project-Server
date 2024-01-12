from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity
from sqlalchemy import text




app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
tourist1 = Tourist(name='Jane Doe', user_type='TOURIST',username='janedoe123', email='jane.doe@gmail.com')
tourist1.set_password('password')

db.session.add(tourist1)
db.session.commit()

name = "NYC"
tags = ["#photo"]
description="The city that never sleeps"
location = "USA"
images = ["https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg"]

place = Place(name=name, tags=tags, description=description, location=location, images=images)
db.session.add(place)


guide1 = Guide(place_id=1, name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com')
guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc",
                    filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY")

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


def create_guide(place_id, name, user_type, username, email, filters, images=None):
    guide = Guide(place_id=place_id, name=name,
                  user_type=user_type, username=username, email=email, images=images or [])
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
    ("Malta", ["#beach"], "best island", "Europe", [
        "https://assets.vogue.com/photos/599365b2f0b0e21484d3436e/master/w_1920,c_limit/00-lede-a-travel-guide-to-malta.jpg"
    ]),
    ("Los Angeles", ["#city"], "vibrant city", "USA", [
        "https://static.independent.co.uk/2023/07/07/10/iStock-515064346.jpg?quality=75&width=990&crop=3%3A2%2Csmart&auto=webp"
    ]),
    ("Paris", ["#culture"], "City of Love", "France", [
        "https://images.ctfassets.net/qr8kennq1pom/77Pd54E3jufwEzXFWvK4XC/88bc77718a8339e945a6749be2c9b344/Untitled_design_-_2022-06-14T124536.639.png"
    ]),
    ("Sydney", ["#beach"], "Beautiful beaches", "Australia", [
        "https://wakeup.com.au/wp-content/themes/yootheme/cache/3shutterstock_1094901527-bd70b9b3.jpeg"
    ]),
    ("Rome", ["#history"], "Eternal City", "Italy", [
        "https://media.timeout.com/images/105211701/1024/576/image.webp"
    ]),
    ("Oslo", ["#city"], "Rich Arts Culture", "Norway", [
        "https://a.cdn-hotels.com/gdcs/production106/d1597/5303351b-a7d2-4775-994a-348002ea13d2.jpg"
        ]),
    ("Budapest", ["#culture"], "Incredible Architecture", "Hungary", [
        "https://www.budapest.org/en/wp-content/uploads/sites/101/budapest-danube-panorama-hd.jpg"
    ]),
    ("Hong Kong", ["#city"], "You can leave Hong Kong, but it will never leave you", "Hong Kong",  [
        "https://ik.imgkit.net/3vlqs5axxjf/external/http://images.ntmllc.com/v4/destination/Hong-Kong/Hong-Kong-city/112086_SCN_HongKong_iStock466733790_Z8C705.jpg?tr=w-1200%2Cfo-auto"
    ]),
    ("Siem Reap", ["#history", "#culture"], "Immense Buddhist and Hindu culture", "Cambodia", [
        "https://afar.brightspotcdn.com/dims4/default/1703b8c/2147483647/strip/true/crop/1000x500+0+84/resize/1440x720!/quality/90/?url=https%3A%2F%2Fafar-media-production-web.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fe5%2Fa0%2Ff8bf9b9e683d6b8ada1c501e8a0b%2Foriginal-les1808.jpg"
    ]),
    ("Hanoi", ["#city"], "One of the world's most ancient capitals", "Vietnam", [
        "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/05/11/10/hanoi-main.jpg?quality=75&width=1200&auto=webp"
    ]), 
    ("Chiang Mai", ["#history", "#culture"], "Home to the most beautiful mountains in the world", "Thailand", [
        "https://a.cdn-hotels.com/gdcs/production9/d679/184d7edf-5c3a-470c-8529-b0085d6d5b0e.jpg"
    ]),
    ("Prague", ["#culture"], "The Home of Christmas", "Czechia", [
        "https://cdn.mos.cms.futurecdn.net/5WUroWJ3ECE9pk9vBhXiqP-1200-80.png"
    ])

]

for data in place_data:
    create_place(*data)

db.session.commit()

# Add more guides
guide_data = [
    (2, 'Hiroshi Tanaka', 'GUIDE', 'hiroshi88','hiroshi.tanakaj@gmail.com', ['CULTURAL', 'SHOPPING'], [
        "https://i1.rgstatic.net/ii/profile.image/11431281103851697-1669864605754_Q512/Hiroshi-Tanaka-9.jpg"
    ]),
    (2, 'Yuki Nakamura', 'GUIDE', 'yuki42','yuki.nakamura@gmail.com', ['HISTORICAL', 'FOOD'],
     ["https://m.media-amazon.com/images/M/MV5BMGY4ODZjYjEtOTc3MC00ZTFiLThiYjktMDk1ZTQ1NjY1YjM2XkEyXkFqcGdeQXVyMTEwODg2MDY@._V1_.jpg"]),
    (2, 'Haruki Ito', 'GUIDE', 'haruki123', 'haruki.ito@gmail.com', ['NATURE', 'ENTERTAINMENT'], [
    "https://i1.sndcdn.com/avatars-000336898423-5m8j59-t500x500.jpg"
    ]),
    (2, 'Kaori Fujimoto', 'GUIDE', 'fujimoto456', 'koari.fujimoto@gmail.com', ['ART', 'OUTDOOR_ACTIVITIES'], 
     [
         "https://sliverofstonemagazinedotcom.files.wordpress.com/2015/03/kaori-fujimoto.jpg?w=1016"
     ]),
    (2, 'Ryota Kobayashi', 'GUIDE', 'kobayashi789','ryota.kobayashi@gmail.com', ['CULTURAL', 'NIGHTLIFE'], 
     [
         "https://static.wikia.nocookie.net/kamenrider/images/c/c4/Kobayashi_Ryota.jpg/revision/latest?cb=20180508155304"
     ])
]

for data in guide_data:
    create_guide(*data)

db.session.commit()

# Add more activities
activity_data = [
    ("hiking", "Los Angeles", ["OUTDOOR_ACTIVITIES"], 2, "amazing views", "90210", "https://www.travelandleisure.com/thmb/rQzeiOHY69ySOnDQ2b3PkEEw6L0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/mount-hollywood-griffith-park-los-angeles-california-LAHIKES0720-a7d3456d01dc4fa0b1171b0324a3b7c8.jpg"),
    ("museum tour", "Paris", ["CULTURAL", "HISTORICAL"],3, "art and history exploration", "75001", "https://www.hotelbleudegrenelle.com/cache/img/3bc673b7b07a78556061cf6ef2253786118c6cd1-3bc673-1024-383-landscape.jpg"),
    ("sushi cooking class", "Tokyo", ["FOOD", "CULTURAL"], 4, "learn the art of sushi making", "100-0005", "https://media.tacdn.com/media/attractions-splice-spp-674x446/0a/9d/33/89.jpg"),
    ("beach volleyball", "Sydney", ["OUTDOOR_ACTIVITIES", "SPORTS"], 5, "fun in the sun", "2000", "https://i.guim.co.uk/img/media/8e4116403e3ed91e98ca58ca7f4583824ca5da88/0_367_4207_2525/master/4207.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=657fb8f44b70414b7d6a416c1bc11ee0"),
    ("Colosseum tour", "Rome", ["HISTORICAL","CULTURAL"], 6, "ancient wonders", "00184", "https://cdn.mos.cms.futurecdn.net/BiNbcY5fXy9Lra47jqHKGK-1200-80.jpg"),
    ("Rock Climbing", "Oslo", ["OUTDOOR_ACTIVITIES", "SPORTS"], 7, "adrenaline-fuelled fun", "0010", "https://www.adamondra.com/boulderinginhell-v2a-f-mp4-000288640-res-photo-pg-1140-1920-.jpg"),
    ("Ruin Bar Tour", "Budapest", ["HISTORICAL"], 8 , "Experience the bustling nightlife of Budapest", "1051", "https://traveladdicts.net/wp-content/uploads/2017/03/Budapest-ruin-pubs-Szimpla-kert-interior-from-above.jpg"),
    ("Island Hopping", "Hong Kong", ["OUTDOOR_ACTIVITIES"], 9, "Feel the breeze as you speed around the breathtaking islands of Hong Kong", "999077", "https://images.rove.me/w_1920,q_85/fanxtgi7z4x83ulwocrz/hong-kong-outlying-islands.jpg"),
    ("Floating Village Tour", "Siem Reap", ["CULTURAL"], 10, "See the floating villages and restuarants of Kampong Phluk", "171001", "https://i0.wp.com/www.myticklefeet.com/wp-content/uploads/2019/02/IMG_3444.jpg?fit=1400%2C933&ssl=1"),
    ("Egg Coffee Making Class", "Hanoi", ["CULTURAL", "FOOD"], 11, "Calling all coffee lovers! Experience the rich tastes and techniques of authentic Vietnamese Coffee", "100000", "https://japanesecoffeeco.com/cdn/shop/articles/Everything_you_need_to_know_about_Vietnamese_Egg_Coffee.jpg?v=1678854456"),
    ("Muay Thai Fight Night", "Chiang Mai", ["CULTURAL"], 12, "Find yourself in the front row of a real Thai boxing match in the centre of Thapae boxing stadium", "50230", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/b3/fe/fe/castigando-el-higado.jpg?w=1200&h=-1&s=1"),
    ("Beer Tasting Experience", "Prague", ["CULTURAL", "FOOD"], 13, "Home to some of the best tasting beer on the planet, Prague has a vast selection of beers to quench your thirst", "100 00", "https://i0.wp.com/jetsettingfools.com/wp-content/uploads/2017/03/Beer-at-Sunset-at-T-Anker-Craft-Beer-Prague-Czech-Republic.jpg?resize=1024%2C683&ssl=1")



    ]

for data in activity_data:
    create_activity(*data)

db.session.commit()



db.session.commit()
