from application.places.model import Place
from application.activities.model import Activity
# from application.plans.model import Plan
def test_new_place():

    new_place = Place(name="amsterdam", location="Netherlands", description="European city", tags="#awesome")
    # assert new_place.place_id == 1


    assert new_place.json == {
        "place_id": new_place.place_id,
        "name": new_place.name,
        "location": new_place.location,
        "description": new_place.description,
        "tags": new_place.tags
        }
    
def test_new_activity():

    new_activity = Activity(name="amsterdam", location="Netherlands", description="European city", post_code="111", place_id=1)
    # assert new_place.place_id == 1


    assert new_activity.json == {
        "activity_id": new_activity.activity_id,
        "name": new_activity.name,
        "location": new_activity.location,
        "place_id": new_activity.place_id,
        "description": new_activity.description,
        "post_code": new_activity.post_code
        }

# def test_new_plan():

#     new_plan = Plan(tourist_id=1, guide_id=1, activity_id=1, status=1)
#     # assert new_place.place_id == 1


#     assert new_plan.json == {
#         "plan_id": new_plan.plan_id,
#         "tourist_id": new_plan.tourist_id,
#         "guide_id": new_plan.guide_id,
#         "timestamp": new_plan.timestamp,
#         "activity_id": new_plan.activity_id,
#         "status": new_plan.status
#         }
