
current_game = {
    'smallBlind': 1,
    'bigBlind': 2,
    'yourCards': [
        {'rank': 'deuce', 'suit': 'clubs'},
        {'rank': 'seven', 'suit': 'hearts'}
    ],
    'tableCards': [
        {'rank': 'ace', 'suit': 'clubs'},
        {'rank': 'eight', 'suit': 'hearts'},
        {'rank': 'queen', 'suit': 'diamonds'},
        {'rank': 'three', 'suit': 'spades'},
        {'rank': 'king', 'suit': 'hearts'}
    ],
    'players': [
        {
            'username': 'usernameOfSmallBlindBot',
            'chips': 100,
            'pot': 20,
            'isAllIn': False,
            'hasFolded': False
        },
        {
            'username': 'usernameOfbigBlindBot',
            'chips': 22,
            'pot': 10,
            'isAllIn': False,
            'hasFolded': True
        },
        {
            'username': 'bot3',
            'chips': 0,
            'pot': 20,
            'isAllIn': True,
            'hasFolded': False
        },
        {
            'username': 'yourUsername',
            'chips': 45,
            'pot': 10,
            'isAllIn': False,
            'hasFolded': False
        }
    ]
}


def action():
    return {'action': 'fold'}