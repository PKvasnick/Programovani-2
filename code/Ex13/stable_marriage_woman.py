from collections import deque


def gale_shapley(men_preferences, women_preferences):
    n = len(women_preferences)
    free_women = deque(women_preferences.keys())  # All women start out free
    engaged_pairs = {}  # Engaged pairs woman -> man
    women_proposals = {woman: [] for woman in women_preferences}  # Track proposals

    # While there are free women who haven't proposed to all men
    while free_women:
        woman = free_women.popleft()  # Grab the first free woman
        woman_pref = women_preferences[woman]
        for man in woman_pref:
            if man not in women_proposals[woman]:
                women_proposals[woman].append(man)  # Record the proposal
                # If the man is free, engage them
                if man not in engaged_pairs.values():
                    engaged_pairs[woman] = man
                    # free_women.remove(woman)
                    break
                else:
                    # If the man is already engaged, check if he prefers the new woman
                    current_woman = next(
                        w for w, m in engaged_pairs.items() if m == man
                    )
                    man_pref = men_preferences[man]
                    if man_pref.index(woman) < man_pref.index(current_woman):
                        # Engage the new woman and free the current one
                        engaged_pairs[woman] = man
                        # free_women.remove(woman)
                        free_women.append(current_woman)
                        del engaged_pairs[current_woman]
                        break

    return engaged_pairs


def main():
    # Example usage
    men_preferences = {
        "Oscar": ["Wanda", "Karen", "Lacey", "Emma"],
        "Davis": ["Wanda", "Lacey", "Karen", "Emma"],
        "Brent": ["Lacey", "Karen", "Wanda", "Emma"],
        "Hank": ["Lacey", "Wanda", "Emma", "Karen"],
    }

    women_preferences = {
        "Wanda": ["Brent", "Hank", "Oscar", "Davis"],
        "Emma": ["Davis", "Hank", "Oscar", "Brent"],
        "Lacey": ["Brent", "Davis", "Hank", "Oscar"],
        "Karen": ["Brent", "Hank", "Davis", "Oscar"],
    }

    result = gale_shapley(men_preferences, women_preferences)
    print(result)


if __name__ == "__main__":
    main()
