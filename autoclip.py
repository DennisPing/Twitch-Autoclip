import os
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
from itertools import cycle
import datetime
from time import time

def get_emote_names(emote, multi_emotes):
    names = []
    if emote in multi_emotes:
        names = multi_emotes[emote]
    else:
        names.append(emote)
    return names

def graph_rate(chatcount):
    plt.style.use("ggplot")
    plt.figure(figsize=(14,8))

    x, y = zip(*chatcount)
    plt.plot(x,y)

    xformatter = DateFormatter('%H:%M:%S')
    
    plt.xlabel("Time", fontsize=16)
    plt.ylabel("Chat Count", fontsize=16)
    plt.xticks(rotation = 45)
    plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
    plt.show()

def main():
    t1 = time()
    chatcount = []
    cwd = os.getcwd()
    with open(f"{cwd}/chatlogs/1067165231.log") as chatlog:
        timer = 30
        count = 0

        startToggle = cycle([0, 29])
        endToggle = cycle([30, 59])
        start = next(startToggle)
        end = next(endToggle)
        base = datetime.datetime(2021, 1, 1)

        for line in chatlog:
            count += 1
            timestamp = line.split(' ', 1)
            _, _, ss = timestamp[0].split(':')

            if start <= int(ss) <= end:
                continue # keep looping
            else:
                start = next(startToggle)
                end = next(endToggle)
                chatcount.append((base + datetime.timedelta(seconds=timer), count)) # add coordinates
                timer += 30
                count = 0 # reset the count
        ts = base + datetime.timedelta(seconds=timer) # catch the last count
        chatcount.append((ts, count))
    duration = time() - t1
    print(f"Time taken: {round(duration, 3)} seconds")

    graph_rate(chatcount)

            
        

if __name__ == "__main__":
    main()