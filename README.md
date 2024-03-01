# GameScoreCentral

# Setup

> The setup below is focused only for the UNIX based systems, for windows, the setup might be different.

### Python version

Uses Python version 3.11.0 for this project

### Virtual environment

1. Create a virtual env `python3 -m venv .venv` in the current directory.
2. Activate the virtual env `source .venv/bin/activate`.
3. Run `which python3` to verify that the virtual env is activated. (should return the path to the virtual env)
4. Install the dependencies `pip install -r requirements.txt`.

# Current Setup

- main app (name: GameScoreCentral)
  - signin/ (name: signin)
  - signup/ (name: signup)
  - home/ (name: home)
  - account/
    - profile/ (name: profile)
    - edit/ (name: editProfile)
    - view/:id (name: viewProfile)
  - game/
    - viewAllGames/ (name: viewAllGames)
    - :id/ (name: viewGame)
    - new/ (name: addNewGame)
- GameScoreCentral
  - views.py
- account
  - profilePage
  - editProfile
  - viewProfile
- game
  - viewAllGames
  - viewGame
  - addNewGame
