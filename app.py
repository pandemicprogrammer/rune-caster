import random


# Dictionary of Runes, Meanings and Inverted Meanings
runes = {
    'Fehu': ['Wealth, prosperity', 'Loss of wealth, failure'],
    'Uruz': ['Physical strength, speed', 'Weakness, inconsistency'],
    'Thurisaz': ['Force, chaos', 'Destruction, defenselessness'],
    'Ansuz': ['Wisdom, communication', 'Misunderstanding, manipulation'],
    'Raidho': ['Travel, movement', 'Unexpected change, delay'],
    'Kenaz': ['Knowledge, illumination', 'Ignorance, instability'],
    'Gebo': ['Gifts, exchange', 'Obligation, ingratitude'],
    'Wunjo': ['Joy, harmony', 'Sorrow, strife'],
    'Hagalaz': ['Disruption, change', 'Stagnation, loss of power'],
    'Nauthiz': ['Need, resistance', 'Impatience, compulsion'],
    'Isa': ['Stillness, isolation', 'Boredom, loneliness'],
    'Jera': ['Harvest, reward', 'Indolence, missed opportunity'],
    'Eihwaz': ['Endurance, defense', 'Confusion, destruction'],
    'Perthro': ['Mystery, chance', 'Stasis, lack of change'],
    'Algiz': ['Protection, growth', 'Hidden danger, loss of shield'],
    'Sowilo': ['Energy, life force', 'Weakness, lack of energy'],
    'Tiwaz': ['Justice, sacrifice', 'Injustice, lack of conviction'],
    'Berkano': ['Birth, fertility', 'Sterility, stagnation'],
    'Ehwaz': ['Harmony, teamwork', 'Discord, betrayal'],
    'Mannaz': ['Humanity, social order', 'Isolation, selfishness'],
    'Laguz': ['Flow, life energy', 'Fear, lack of creativity'],
    'Ingwaz': ['Potential, fertility', 'Impotence, lack of action'],
    'Dagaz': ['Breakthrough, clarity', 'Confusion, lack of vision'],
    'Othala': ['Inheritance, home', 'Loss, lack of direction'],
}
# Dictionary of some basic rune relations for demonstration
rune_relations = {
    ('Fehu', 'Uruz'): 'Wealth and strength can coexist.',
    ('Uruz', 'Thurisaz'): 'Strong forces might lead to chaos.',
    ('Thurisaz', 'Ansuz'): 'Chaotic forces may disrupt communication.',
    ('Ansuz', 'Raidho'): 'Communication can aid in travel or change.',
    ('Raidho', 'Kenaz'): 'Travel or movement may lead to new knowledge.',
    ('Kenaz', 'Gebo'): 'Knowledge is a gift.',
    ('Gebo', 'Wunjo'): 'Gifts may bring joy.',
    ('Wunjo', 'Hagalaz'): 'Even in joy, be aware of potential disruptions.',
    ('Hagalaz', 'Nauthiz'): 'Disruptions may lead to need or resistance.',
    ('Nauthiz', 'Isa'): 'Resistance can lead to stagnation or isolation.',
    ('Isa', 'Jera'): 'Stagnation might prevent harvest or reward.',
    ('Jera', 'Eihwaz'): 'Rewards require endurance.',
    ('Eihwaz', 'Perthro'): 'Endurance can lead to unknown outcomes.',
    ('Perthro', 'Algiz'): 'Mystery and protection can go hand in hand.',
    ('Algiz', 'Sowilo'): 'Protection can lead to vital energy or life force.',
    ('Sowilo', 'Tiwaz'): 'Life energy may require justice or sacrifice.',
    ('Tiwaz', 'Berkano'): 'Justice may result in new beginnings or growth.',
    ('Berkano', 'Ehwaz'): 'Growth and harmony often go together.',
    ('Ehwaz', 'Mannaz'): 'Harmony can enhance social connections and humanity.',
    ('Mannaz', 'Laguz'): 'Social harmony can stimulate creative flow.',
    ('Laguz', 'Ingwaz'): 'Creative flow may lead to potential and fertility.',
    ('Ingwaz', 'Dagaz'): 'Fertility can result in breakthroughs and clarity.',
    ('Dagaz', 'Othala'): 'Clarity can aid in understanding your heritage or home.'
}


def cast_rune(runes):
    num_runes = random.randint(1, 5)  # Choose between 1 and 3 runes
    output = ""
    casted_runes = []
    for _ in range(num_runes):
        rune, meanings = random.choice(list(runes.items()))
        inverted = random.choice([0, 1])
        meaning = meanings[inverted]
        casted_runes.append(rune)
        if inverted:
            output += f'\nRune: {rune} (inverted)\nMeaning: {meaning}\n\n'
        else:
            output += f'\nRune: {rune}\nMeaning: {meaning}\n\n'

    # Check for relations
    for i in range(len(casted_runes)):
        for j in range(i + 1, len(casted_runes)):
            relation = rune_relations.get((casted_runes[i], casted_runes[j]))
            if relation:
                output += f'Relation: {casted_runes[i]} and {casted_runes[j]}: {relation}\n\n'
    
    return output

# Run the function
print(cast_rune(runes))
