#!/usr/bin/env python3.6

from image_quality import get_blurrness_score, perform_color_analysis

if __name__ == '__main__':
    IMG_LOC = '../data/mainlogo.png'
    score = get_blurrness_score(IMG_LOC)
    print(score)

    score2 = perform_color_analysis(IMG_LOC)
    print(score2)
