from application.Place.model import Place

def test_new_place():

    new_place = Place(place_id=1, name="amsterdam", location="Netherlands", description="European city", tags="#awesome")
    assert new_place.place_id == 1


    assert new_place.json == {
        "place_id": new_place.place_id,
        "name": new_place.name,
        "location": new_place.location,
        "description": new_place.description,
        "tags": new_place.tags
        }
