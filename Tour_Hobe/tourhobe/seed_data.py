import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourhobe.settings')
django.setup()

from packages.models import Country, Location, Package
from hotels.models import Hotel, Room

# ── Clear existing data (keep users) ─────────────────────────────────────────
Room.objects.all().delete()
Hotel.objects.all().delete()
Package.objects.all().delete()
Location.objects.all().delete()
Country.objects.all().delete()
print("Cleared old data.")

# ── Countries ─────────────────────────────────────────────────────────────────
bd = Country.objects.create(name='Bangladesh')
th = Country.objects.create(name='Thailand')
my = Country.objects.create(name='Malaysia')
np = Country.objects.create(name='Nepal')
sg = Country.objects.create(name='Singapore')

# ── Locations ─────────────────────────────────────────────────────────────────
cox    = Location.objects.create(country=bd, name="Cox's Bazar",   description="World's longest natural sea beach — 120 km of golden sand and turquoise water.")
sylhet = Location.objects.create(country=bd, name='Sylhet',        description='Tea gardens, haor wetlands and the crystal clear Ratargul Swamp Forest.')
dhaka  = Location.objects.create(country=bd, name='Dhaka',         description='The vibrant capital — Mughal forts, riverside cuisine and endless energy.')
bkk    = Location.objects.create(country=th, name='Bangkok',       description='Gleaming temples, sky-high rooftop bars and legendary floating markets.')
phuket = Location.objects.create(country=th, name='Phuket',        description='Emerald water, white-sand beaches and the famous Phi Phi Island.')
kl     = Location.objects.create(country=my, name='Kuala Lumpur',  description='Iconic twin towers, rainforest parks and multicultural street food.')
ktm    = Location.objects.create(country=np, name='Kathmandu',     description='Gateway to the Himalayas with ancient temples and world-class trekking.')
singa  = Location.objects.create(country=sg, name='Singapore',     description='Futuristic city-state where culture, gardens and gastronomy meet.')

# ── Hotels ────────────────────────────────────────────────────────────────────
# Cox's Bazar
h1 = Hotel.objects.create(
    name="Ocean Pearl Resort", tier='premium', location="Cox's Bazar",
    star_rating=5, price_per_night=8500,
    description='A stunning beachfront 5-star resort with private infinity pools, world-class spa and direct beach access.',
    amenities='Infinity Pool,Spa,Private Beach,WiFi,Fine Dining Restaurant,Beach Bar,Gym'
)
h2 = Hotel.objects.create(
    name="Bay View Inn", tier='standard', location="Cox's Bazar",
    star_rating=3, price_per_night=3200,
    description='Comfortable 3-star hotel with panoramic sea-view rooms and warm Bangladeshi hospitality.',
    amenities='WiFi,Restaurant,Sea View Balcony,AC,24h Front Desk'
)
h3 = Hotel.objects.create(
    name="Surfer's Lodge", tier='budget', location="Cox's Bazar",
    star_rating=2, price_per_night=1200,
    description='Clean, no-fuss budget rooms just steps from the beach — perfect for backpackers.',
    amenities='WiFi,Fan Rooms,Common Rooftop,Tours Desk,Shared Kitchen'
)

# Sylhet
h4 = Hotel.objects.create(
    name='Rose View Hotel', tier='premium', location='Sylhet',
    star_rating=5, price_per_night=7000,
    description='The finest 5-star luxury hotel in Sylhet city with rooftop pool and premium dining.',
    amenities='Rooftop Pool,Gym,Spa,Fine Dining,Banquet Hall,WiFi,Parking'
)
h5 = Hotel.objects.create(
    name='Hillside Retreat', tier='standard', location='Sylhet',
    star_rating=3, price_per_night=2800,
    description='Serene bungalows overlooking lush tea gardens with home-cooked Bengali meals.',
    amenities='WiFi,Breakfast Included,AC,Garden View,BBQ Area'
)
h6 = Hotel.objects.create(
    name="Backpacker's Den", tier='budget', location='Sylhet',
    star_rating=2, price_per_night=900,
    description='A sociable traveller hostel near Jaflong with helpful staff and free local maps.',
    amenities='WiFi,Shared Kitchen,Locker,Dorm Beds,Tours Desk'
)

# Bangkok
h7 = Hotel.objects.create(
    name='The Grand Bangkok', tier='premium', location='Bangkok',
    star_rating=5, price_per_night=12000,
    description='Iconic 5-star riverside hotel with butler service, Michelin-star dining and private river tours.',
    amenities='Infinity Pool,Butler Service,7 Restaurants,Spa,Private River Tour,Helipad,Gym'
)
h8 = Hotel.objects.create(
    name='Silom Suites', tier='standard', location='Bangkok',
    star_rating=3, price_per_night=4500,
    description='Centrally located in the business district, great value with rooftop pool and free breakfast.',
    amenities='WiFi,Rooftop Pool,Gym,Breakfast Included,Airport Shuttle'
)
h9 = Hotel.objects.create(
    name='Khaosan Nest', tier='budget', location='Bangkok',
    star_rating=2, price_per_night=1500,
    description='Lively backpacker hub on the famous Khao San Road — the heartbeat of budget travel in Bangkok.',
    amenities='WiFi,AC,Rooftop Bar,Tours Desk,Shared Lounge'
)

# Phuket
h10 = Hotel.objects.create(
    name='Andaman Cove Resort', tier='premium', location='Phuket',
    star_rating=5, price_per_night=15000,
    description='Exclusive private villas with direct beach access, over-water bungalows and a world-class spa.',
    amenities='Private Pool,Beach Access,Spa,Yacht Rental,Snorkeling,Fine Dining,Butler'
)
h11 = Hotel.objects.create(
    name='Patong Palms Hotel', tier='standard', location='Phuket',
    star_rating=3, price_per_night=5000,
    description='Great value hotel just 5 minutes walk from the famous Patong Beach.',
    amenities='Pool,WiFi,AC,Breakfast,Bar,Island Tour Desk'
)

# Kuala Lumpur
h12 = Hotel.objects.create(
    name='Petronas Skyline Hotel', tier='premium', location='Kuala Lumpur',
    star_rating=5, price_per_night=11000,
    description='Luxury hotel with breathtaking panoramic views of the iconic Petronas Twin Towers.',
    amenities='Sky Pool,Spa,Club Lounge,5 Restaurants,WiFi,Concierge,Airport Limo'
)
h13 = Hotel.objects.create(
    name='Bukit Bintang Inn', tier='budget', location='Kuala Lumpur',
    star_rating=2, price_per_night=1800,
    description='Budget gem in the heart of KL shopping district — minutes from Pavilion and KLCC.',
    amenities='WiFi,AC,Breakfast,24h Reception,Metro Access'
)

# Kathmandu
h14 = Hotel.objects.create(
    name='Yak & Yeti Hotel', tier='premium', location='Kathmandu',
    star_rating=5, price_per_night=9000,
    description='A legendary 5-star heritage hotel in the heart of Kathmandu with Himalayan gardens.',
    amenities='Garden Pool,Spa,Casino,3 Restaurants,Mountain View Rooms,WiFi,Concierge'
)
h15 = Hotel.objects.create(
    name='Thamel Travellers Inn', tier='budget', location='Kathmandu',
    star_rating=2, price_per_night=1100,
    description='Budget-friendly spot in the famous Thamel district — perfect for trekking adventurers.',
    amenities='WiFi,Gear Storage,Trekking Tours,Rooftop Terrace,Hot Water'
)

# ── Rooms ─────────────────────────────────────────────────────────────────────
rooms_data = [
    (h1,  [('Deluxe Sea View Room', 2, 1, 9500, 15), ('Ocean Grand Suite', 2, 0, 18000, 5)]),
    (h2,  [('Standard Room', 2, 0, 3200, 20), ('Family Sea View', 2, 2, 5500, 8)]),
    (h3,  [('Dorm Bed (6-share)', 1, 0, 600, 30), ('Private Room', 2, 0, 1200, 10)]),
    (h4,  [('Luxury Deluxe', 2, 0, 7000, 20), ('Presidential Suite', 2, 2, 20000, 3)]),
    (h5,  [('Garden Bungalow', 2, 0, 2800, 12), ('Family Cottage', 2, 2, 4500, 6)]),
    (h6,  [('Dorm Bed', 1, 0, 450, 40), ('Private Cabin', 2, 0, 900, 8)]),
    (h7,  [('River View Room', 2, 0, 12000, 30), ('Chao Phraya Suite', 2, 0, 22000, 10), ('Penthouse', 2, 2, 40000, 2)]),
    (h8,  [('Superior Room', 2, 0, 4500, 25), ('Deluxe Room', 2, 1, 6000, 15)]),
    (h9,  [('Dorm (4-share)', 1, 0, 750, 20), ('Ensuite Private', 2, 0, 1500, 10)]),
    (h10, [('Beach Villa', 2, 0, 15000, 10), ('Over-Water Bungalow', 2, 0, 20000, 5), ('Pool Villa', 2, 2, 25000, 5)]),
    (h11, [('Standard Room', 2, 0, 5000, 20), ('Superior Pool View', 2, 1, 7000, 10)]),
    (h12, [('Tower View Room', 2, 0, 11000, 25), ('Sky Suite', 2, 1, 25000, 8)]),
    (h13, [('Standard Room', 2, 0, 1800, 20), ('Twin Room', 2, 0, 2200, 10)]),
    (h14, [('Heritage Room', 2, 0, 9000, 20), ('Royal Suite', 2, 2, 28000, 5)]),
    (h15, [('Dorm Bed', 1, 0, 550, 30), ('Standard Room', 2, 0, 1100, 15)]),
]

for hotel, rooms in rooms_data:
    for rtype, adults, children, price, total in rooms:
        Room.objects.create(
            hotel=hotel, room_type=rtype,
            capacity_adults=adults, capacity_children=children,
            price_per_night=price, total_rooms=total
        )

# ── Packages ──────────────────────────────────────────────────────────────────
p1 = Package.objects.create(
    location=cox, title="Cox's Bazar Beach Escape",
    duration='3 Days / 2 Nights', price=8500,
    description="Dive into the world's longest natural sea beach. Enjoy guided tours of local fisher villages, fresh Mezban seafood banquets and breathtaking sunrise and sunset strolls along the shore."
)
p1.hotels.set([h1, h2, h3])

p2 = Package.objects.create(
    location=cox, title="Cox's Bazar Luxury Retreat",
    duration='5 Days / 4 Nights', price=25000,
    description='An exclusive 5-star escape with private beachfront villa stay, yacht sunset cruise, traditional fishing village tour and daily spa sessions at the Ocean Pearl Resort.'
)
p2.hotels.set([h1])

p3 = Package.objects.create(
    location=sylhet, title='Sylhet Tea Garden Explorer',
    duration='3 Days / 2 Nights', price=6500,
    description='Trek through endless rolling tea gardens, boat through the haunting Ratargul Swamp Forest canopy and refresh in the crystal-clear stone river of Jaflong.'
)
p3.hotels.set([h4, h5, h6])

p4 = Package.objects.create(
    location=sylhet, title='Sylhet Spiritual Heritage Tour',
    duration='2 Days / 1 Night', price=4200,
    description='A soulful journey through the shrines of Shah Jalal and Shah Poran, panoramic haor wetland boat rides and the serene seven-layer waterfall of Madhabkunda.'
)
p4.hotels.set([h4, h5])

p5 = Package.objects.create(
    location=bkk, title='Bangkok City Discovery',
    duration='4 Days / 3 Nights', price=35000,
    description='Grand Palace, Wat Pho reclining Buddha, Damnoen Saduak floating market and an unforgettable Chao Phraya River dinner cruise with traditional Thai dance performance.'
)
p5.hotels.set([h7, h8, h9])

p6 = Package.objects.create(
    location=phuket, title='Phuket Island Paradise',
    duration='5 Days / 4 Nights', price=55000,
    description='Phi Phi island hopping by speedboat, kayaking through the magical limestone caves of Phang Nga Bay, Big Buddha visit and an epic Maya Bay sunset snorkel session.'
)
p6.hotels.set([h10, h11])

p7 = Package.objects.create(
    location=kl, title='Kuala Lumpur City & Culture',
    duration='4 Days / 3 Nights', price=32000,
    description='Stand beneath the Petronas Twin Towers, explore Batu Caves Hindu temple complex, wander the street art of Chinatown and indulge in the legendary night markets of Jalan Alor.'
)
p7.hotels.set([h12, h13])

p8 = Package.objects.create(
    location=ktm, title='Kathmandu Heritage & Himalaya Trek',
    duration='6 Days / 5 Nights', price=42000,
    description='Ancient UNESCO Durbar squares, Boudhanath Stupa sunrise meditation, Nagarkot mountain viewpoint at dawn and an exhilarating Langtang Valley overnight trek with Sherpa guide.'
)
p8.hotels.set([h14, h15])

# ── Summary ───────────────────────────────────────────────────────────────────
print("\n==========================")
print("  SEED COMPLETE!")
print("==========================")
print(f"  Countries : {Country.objects.count()}")
print(f"  Locations : {Location.objects.count()}")
print(f"  Hotels    : {Hotel.objects.count()}")
print(f"  Rooms     : {Room.objects.count()}")
print(f"  Packages  : {Package.objects.count()}")
print("\nPackages created:")
for p in Package.objects.select_related('location__country').prefetch_related('hotels'):
    print(f"  [{p.location.country.name}] {p.title} | {p.hotels.count()} hotels")
print("==========================\n")
