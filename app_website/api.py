from ninja import NinjaAPI


api = NinjaAPI()

exercise = {
    1: {
        "name": "bench press",
        "targeted muscle" : "chest"
    },
    2: {
        "name": "squat",
        "targeted muscle" : "legs --> hamstrings"
    },
    3: {
           "name": "bicep curl",
           "targeted muscle": "bicep"
    }
}
@api.get("/exercise/{exercise_id}")
def get_exercise(request, exercise_id: int):
    return exercise[exercise_id]





