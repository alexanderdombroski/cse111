# Created by Alex Dombroski 10/16/24
import random as r

# ---------- Functions to return words ----------

def ad_get_noun(p_noun_quantity): # Gets a random noun representing a person or an animal, used for as subject or in prepisitional phrases. 
    if p_noun_quantity == 1:
        ad_word = r.choice(["dog", "cat", "parrot", "worker", "man", "woman", "girl", "boy", "teammate", "teacher", "kid", "robot"])
    else:
        ad_word = r.choice(["dogs", "cats", "parrots", "workers", "men", "women", "girls", "boys", "teamates", "teachers", "kids", "robots"])
    return ad_word

def ad_get_location(): # Gets a random noun representing a location, sometimes used in prepisitional phrases.
    return r.choice(["river", "pond", "house", "kitchen", "city", "building", "school", "church", "restaurant", "forest", "tunnel", "cave"])

def ad_get_verb(p_tense): # Gets a verb depending on tense. (Noun quantity doesn't matter, because it is resolved with the auxillary verbs.)
    if p_tense == "future":
        ad_word = r.choice(["run", "speak", "stare", "sit", "play", "sleep", "eat", "smell"])
    elif p_tense == "present":
        ad_word =  r.choice(["running", "speaking", "staring", "sitting", "playing", "sleeping", "eating", "smelling"])
    else:
        ad_word = r.choice(["ran", "spoke", "stared", "sat", "played", "slept", "ate", "smelled"])
    return ad_word

def ad_get_auxillary_verb(p_noun_quantity, p_tense): # Gets random helping verb to add detail to p_tense and amount 
    if p_tense == "future":
        ad_word = r.choice(["will", "might", "should"])
    elif p_tense == "present":
        ad_word = "is" if p_noun_quantity == 1 else "are"
    else:
        ad_word = ""
    return ad_word

def ad_get_determiner(p_noun_quantity): # Return words based off noun quantity
    if p_noun_quantity == 1:
        ad_word = r.choice(["a", "the"])
    else:
        ad_word = r.choice(["many", "some", "a few"])
    return ad_word

def ad_get_adjective(): # Returns random adjective
    return r.choice(["tall", "loud", "cool", "colorful", "small", "clean", "rough", "cumbersome", "old", "damaged", "humble", "pungent"])

def ad_get_adverb(p_adverb_type = ""):
    if p_adverb_type == "time":
        ad_word = r.choice(["never", "sometimes", "often", "rarely", "frequently"])
    else:
        ad_word = r.choice(["continuously", "happily", "cautiously", "suddenly", "poorly", "quietly", "intently", "boldly"])
    return ad_word

def ad_get_preposition(): # Returns random preposition
    return r.choice(["beside", "behind", "around", "close by", "underneath", "in front of", "near", "far from"])

# ---------- Functions to combine words ----------

def ad_get_prepositional_phrase(p_noun_quantity): # Combines preposition, determiner, and noun
    if r.random() > .5:
        ad_determiner = ad_get_determiner(p_noun_quantity)
        ad_noun = ad_get_noun(p_noun_quantity)
    else:
        ad_determiner = "the"
        ad_noun = ad_get_location() 
    ad_noun = f"{ad_get_adjective() if r.random() > .7 else ''} {ad_noun}".strip()
    return f"{ad_get_preposition()} {ad_determiner} {ad_noun}"

def ad_make_verb_phrase(p_subject_amount, p_verb_tense): # Combines auxilary verbs, adverbs, and verbs.
    ad_verb = ad_get_verb(p_verb_tense)
    ad_verb_phrase = f"{ad_verb} {ad_get_adverb() if r.random() > .5 else ''}".strip() # add adverb
    ad_verb_phrase = f"{ad_get_adverb('time') if r.random() > .5 else ''} {ad_verb_phrase}".strip() # add time/freqency adverb
    ad_verb_phrase = f"{ad_get_auxillary_verb(p_subject_amount, p_verb_tense)} {ad_verb_phrase}".strip() # add auxillary verb
    return ad_verb_phrase

def ad_make_subject_phrase(p_subject_amount): # Combines determiner, noun, and potentially an adjective
    ad_subject = f"{ad_get_adjective() if r.random() > .3 else ''} {ad_get_noun(p_subject_amount)}".strip()
    return f"{ad_get_determiner(p_subject_amount).capitalize()} {ad_subject}"

def ad_make_sentence(p_subject_amount, p_verb_tense): # Combines subject phrase, verb phrase, and prepositional phrase(s).
    ad_subject_phrase = ad_make_subject_phrase(p_subject_amount)
    ad_verb_phrase = ad_make_verb_phrase(p_subject_amount, p_verb_tense)
    ad_prepositional_phrase = ad_get_prepositional_phrase(p_subject_amount)
    ad_prepositional_phrase_2 = ad_get_prepositional_phrase(p_subject_amount) if r.random() > .65 else ""
    return f"{ad_subject_phrase} {ad_verb_phrase} {ad_prepositional_phrase} {ad_prepositional_phrase_2}".strip() + "."

def main():
    # print()
    # for ad_subject_amount in [1, 2]: # Calls ad_make_sentence() 6 times and uses the different arguements each time
    #     for ad_verb_tense in ["past", "present", "future"]:
    #         print(ad_make_sentence(ad_subject_amount, ad_verb_tense))
    # print()
    print(ad_make_sentence(1, "past"))
    print(ad_make_sentence(1, "present"))
    print(ad_make_sentence(1, "future"))
    print(ad_make_sentence(2, "past"))
    print(ad_make_sentence(2, "present"))
    print(ad_make_sentence(2, "future"))

if __name__ == "__main__":
    main()


