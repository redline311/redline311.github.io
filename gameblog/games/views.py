from django.shortcuts import render

# Create your views here.

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Call of Duty: Modern Warfare 2",
            "images": "mw2.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 2,
            "title": "Grand Theft Auto 5",
            "images": "gta5.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 3,
            "title": "Insurgency: Sandstorm",
            "images": "insurgency_sand.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 4,
            "title": "Squad",
            "images": "squad.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 5,
            "title": "Counter-Strike 2",
            "images": "cs2.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 6,
            "title": "FIFA 23",
            "images": "fifa23.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 7,
            "title": "Red Dead Redemption 2",
            "images": "rdr2.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },
        {
            "id": 8,
            "title": "Forza Horizon 5",
            "images": "forza_horizon_5.jpeg",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
        },

    ]
}


def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "games/index.html",context)


def games(request):
    return render(request, "games/games.html")
