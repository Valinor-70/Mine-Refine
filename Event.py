special_events = [
    {
        'name': 'Gold Rush',
        'message': 'You hit a gold rush! Your earnings are doubled for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 2)
    },
    {
        'name': 'Cave In',
        'message': 'There was a cave in! You lose all earnings for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0)
    },
    {
        'name': 'Lucky Find',
        'message': 'You found a rare artifact! Your earnings are tripled for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 3)
    },
    {
        'name': 'Market Crash',
        'message': 'The market crashed! Your earnings are halved for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.5)
    },
    {
        'name': 'Inflation',
        'message': 'Inflation is high! Your earnings are reduced by 20% for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.8)
    },
    {
        'name': 'Tax Increase',
        'message': 'Taxes have increased! Your earnings are reduced by 30% for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.7)
    },
    {
        'name': 'Lucky Day',
        'message': 'It\'s your lucky day! You earn a bonus of $100.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money + 100)
    },
    {
        'name': 'Unlucky Day',
        'message': 'It\'s an unlucky day! You lose $100.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money - 100)
    },
    {
        'name': 'Earthquake',
        'message': 'An earthquake strikes! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Tornado',
        'message': 'A tornado hits! You lose 75% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.25)
    },
    {
        'name': 'Drought',
        'message': 'A drought occurs! Your earnings are reduced by 30% for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.7)
    },
    {
        'name': 'Flood',
        'message': 'A flood happens! Your earnings are halved for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.5)
    },
    {
        'name': 'Hurricane',
        'message': 'A hurricane strikes! You lose 75% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.25)
    },
    {
        'name': 'Wildfire',
        'message': 'A wildfire breaks out! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Tsunami',
        'message': 'A tsunami hits! You lose 75% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.25)
    },
    {
        'name': 'Volcanic Eruption',
        'message': 'A volcanic eruption occurs! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Blizzard',
        'message': 'A blizzard strikes! Your earnings are reduced by 30% for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.7)
    },
    {
        'name': 'Heatwave',
        'message': 'A heatwave occurs! Your earnings are halved for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.5)
    },
    {
        'name': 'Avalanche',
        'message': 'An avalanche happens! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Meteor Shower',
        'message': 'A meteor shower occurs! You earn a bonus of $200.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money + 200)
    },
    {
        'name': 'Solar Flare',
        'message': 'A solar flare happens! Your earnings are tripled for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 3)
    },
    {
        'name': 'Eclipse',
        'message': 'An eclipse occurs! Your earnings are doubled for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 2)
    },
    {
        'name': 'Comet',
        'message': 'A comet passes by! You earn a bonus of $300.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money + 300)
    },
    {
        'name': 'Aurora Borealis',
        'message': 'An aurora borealis occurs! Your earnings are doubled for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 2)
    },
    {
        'name': 'Tidal Wave',
        'message': 'A tidal wave hits! You lose 75% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.25)
    },
    {
        'name': 'Sandstorm',
        'message': 'A sandstorm occurs! Your earnings are halved for the next turn.',
        'effect': lambda player: setattr(player, 'multiplier', 0.5)
    },
    {
        'name': 'Dust Devil',
        'message': 'A dust devil happens! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Mudslide',
        'message': 'A mudslide occurs! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    },
    {
        'name': 'Hailstorm',
        'message': 'A hailstorm happens! You lose 50% of your earnings.',
        'effect': lambda player: setattr(player, 'total_money', player.total_money * 0.5)
    }
]
